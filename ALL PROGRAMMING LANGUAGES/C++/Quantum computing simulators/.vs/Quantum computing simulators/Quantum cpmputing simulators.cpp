#include <corecrt_math_defines.h>
#include <iostream>
#include <vector>
#include <complex>
#include <memory>
#include <random>
#include <chrono>
#include <omp.h>
#include <cstring>
#include <unordered_map>
#include <bitset>
#include <cmath>
#include <string>
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx2,fma")
using namespace std;
using Complex = complex<double>;
using StateVector = vector<Complex>;
class QuantumSimulator {
private:
    int num_qubits_;
    size_t state_size_;
    StateVector state_;
    mt19937 rng_;
    unordered_map<string, vector<Complex>> gate_cache_;

public:
    explicit QuantumSimulator(int num_qubits)
        : num_qubits_(num_qubits),
          state_size_(1ULL << num_qubits),
          state_(state_size_),
          rng_(chrono::steady_clock::now().time_since_epoch().count()) {
        reset();
        initialize_gate_cache();
    }

    void reset() {
        fill(state_.begin(), state_.end(), Complex(0.0, 0.0));
        state_[0] = Complex(1.0, 0.0);
    }

    inline void apply_single_qubit_gate(int qubit, const Complex gate[4]) {
        const size_t stride = 1ULL << qubit;
#pragma omp parallel for schedule(static) if(state_size_ > 1024)
        for (size_t i = 0; i < state_size_; i += 2 * stride) {
            for (size_t j = 0; j < stride; ++j) {
                size_t idx0 = i + j;
                size_t idx1 = i + j + stride;
                if (idx1 < state_size_) {
                    Complex a = state_[idx0];
                    Complex b = state_[idx1];
                    state_[idx0] = gate[0] * a + gate[1] * b;
                    state_[idx1] = gate[2] * a + gate[3] * b;
                }
            }
        }
    }

    // Use generic hadamard (safer and portable)
    void hadamard(int qubit) {
        auto it = gate_cache_.find("H");
        Complex g[4];
        if (it != gate_cache_.end()) {
            // copy into C-array
            for (int k = 0; k < 4; ++k) g[k] = it->second[k];
        } else {
            double inv = 1.0 / sqrt(2.0);
            g[0] = Complex(inv, 0); g[1] = Complex(inv, 0);
            g[2] = Complex(inv, 0); g[3] = Complex(-inv, 0);
        }
        apply_single_qubit_gate(qubit, g);
    }

    void pauli_x(int qubit) {
        const size_t mask = 1ULL << qubit;
#pragma omp parallel for schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            if ((i & mask) == 0) {
                size_t j = i | mask;
                // swap each pair once: ensure i < j to avoid double-swap
                if (i < j) {
                    swap(state_[i], state_[j]);
                }
            }
        }
    }

    void pauli_y(int qubit) {
        Complex g[4] = { Complex(0,0), Complex(0,-1), Complex(0,1), Complex(0,0) };
        apply_single_qubit_gate(qubit, g);
    }

    void pauli_z(int qubit) {
        const size_t mask = 1ULL << qubit;
#pragma omp parallel for simd schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            if (i & mask) state_[i] = -state_[i];
        }
    }

    void cnot(int control, int target) {
        const size_t control_mask = 1ULL << control;
        const size_t target_mask = 1ULL << target;
#pragma omp parallel for schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            if ((i & control_mask) && !(i & target_mask)) {
                size_t j = i | target_mask;
                // swap pair (i,j) only when i < j to avoid double swap
                if (i < j) swap(state_[i], state_[j]);
            }
        }
    }

    void rotation_x(int qubit, double theta) {
        double ch = cos(theta / 2.0);
        double sh = sin(theta / 2.0);
        Complex g[4] = { Complex(ch, 0), Complex(0, -sh), Complex(0, -sh), Complex(ch, 0) };
        apply_single_qubit_gate(qubit, g);
    }

    void rotation_y(int qubit, double theta) {
        double ch = cos(theta / 2.0);
        double sh = sin(theta / 2.0);
        Complex g[4] = { Complex(ch, 0), Complex(-sh, 0), Complex(sh, 0), Complex(ch, 0) };
        apply_single_qubit_gate(qubit, g);
    }

    void rotation_z(int qubit, double theta) {
        // Use diagonal form: exp(-i theta/2) for |0>, exp(i theta/2) for |1>
        Complex phase0 = exp(Complex(0, -theta / 2.0));
        Complex phase1 = exp(Complex(0, theta / 2.0));
        const size_t mask = 1ULL << qubit;
#pragma omp parallel for schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            if (i & mask) state_[i] *= phase1;
            else state_[i] *= phase0;
        }
    }

    int measure(int qubit) {
        const size_t mask = 1ULL << qubit;
        double prob_zero = 0.0;
#pragma omp parallel for reduction(+:prob_zero) schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            if (!(i & mask)) prob_zero += norm(state_[i]);
        }
        uniform_real_distribution<double> dist(0.0, 1.0);
        bool measure_zero = dist(rng_) < prob_zero;
        double norm_factor = measure_zero ? sqrt(prob_zero) : sqrt(1.0 - prob_zero);
        if (norm_factor == 0.0) {
            // avoid division by zero: collapse to nearest basis (conservative)
#pragma omp parallel for schedule(static)
            for (size_t i = 0; i < state_size_; ++i) state_[i] = Complex(0.0, 0.0);
            // choose 0 by default
            state_[0] = Complex(1.0, 0.0);
            return 0;
        }
#pragma omp parallel for schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            bool keep = ((i & mask) == 0) == measure_zero;
            if (keep) state_[i] /= norm_factor;
            else state_[i] = Complex(0.0, 0.0);
        }
        return measure_zero ? 0 : 1;
    }

    double expectation_z(int qubit) const {
        const size_t mask = 1ULL << qubit;
        double exp = 0.0;
#pragma omp parallel for reduction(+:exp) schedule(static)
        for (size_t i = 0; i < state_size_; ++i) {
            double sign = (i & mask) ? -1.0 : 1.0;
            exp += sign * norm(state_[i]);
        }
        return exp;
    }

    vector<pair<size_t, Complex>> get_sparse_state(double threshold = 1e-10) const {
        vector<pair<size_t, Complex>> sparse;
        for (size_t i = 0; i < state_size_; ++i) {
            if (norm(state_[i]) > threshold) sparse.emplace_back(i, state_[i]);
        }
        return sparse;
    }

    double get_fidelity() const {
        double f = 0.0;
#pragma omp parallel for reduction(+:f) schedule(static)
        for (size_t i = 0; i < state_size_; ++i) f += norm(state_[i]);
        return f;
    }

    void print_state() const {
        cout << "Quantum State (non-zero amplitudes):\n";
        for (size_t i = 0; i < state_size_; ++i) {
            if (norm(state_[i]) > 1e-10) {
                // create binary string of length num_qubits_
                string b;
                b.reserve(num_qubits_);
                for (int q = num_qubits_ - 1; q >= 0; --q) b.push_back((i & (1ULL << q)) ? '1' : '0');
                cout << "|" << b << "⟩: " << state_[i] << "\n";
            }
        }
        cout << "Fidelity: " << get_fidelity() << "\n\n";
    }

private:
    void initialize_gate_cache() {
        double inv = 1.0 / sqrt(2.0);
        gate_cache_["H"] = { Complex(inv,0), Complex(inv,0), Complex(inv,0), Complex(-inv,0) };
        gate_cache_["X"] = { Complex(0,0), Complex(1,0), Complex(1,0), Complex(0,0) };
        gate_cache_["Y"] = { Complex(0,0), Complex(0,-1), Complex(0,1), Complex(0,0) };
        gate_cache_["Z"] = { Complex(1,0), Complex(0,0), Complex(0,0), Complex(-1,0) };
    }
};

// Benchmark helper
void benchmark_simulator() {
    cout << "=== Quantum Simulator Performance Benchmark ===\n";
    const int num_qubits = 16;
    QuantumSimulator sim(num_qubits);
    auto start = chrono::high_resolution_clock::now();

    for (int i = 0; i < num_qubits; ++i) sim.hadamard(i);

    mt19937 rng(12345);
    uniform_real_distribution<double> angle_dist(0, 2 * M_PI);
    for (int i = 0; i < 100; ++i) {
        int qubit = rng() % num_qubits;
        double angle = angle_dist(rng);
        sim.rotation_y(qubit, angle);
    }

    for (int i = 0; i < num_qubits - 1; ++i) sim.cnot(i, i + 1);

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);

    cout << "Simulation time: " << duration.count() << " ms\n";
    cout << "Final fidelity: " << sim.get_fidelity() << "\n";
    cout << "Number of qubits: " << num_qubits << "\n";
    cout << "State vector size: " << (1ULL << num_qubits) << "\n";
}

int main() {
    cout << "Advanced Quantum Computing Simulator with Optimizations\n";
    cout << "========================================================\n\n";

    QuantumSimulator sim(3);
    cout << "Initial state:\n";
    sim.print_state();

    cout << "After Hadamard on qubit 0:\n";
    sim.hadamard(0);
    sim.print_state();

    cout << "After CNOT(0,1):\n";
    sim.cnot(0, 1);
    sim.print_state();

    cout << "After rotation Y(π/4) on qubit 2:\n";
    sim.rotation_y(2, M_PI / 4);
    sim.print_state();

    cout << "Expectation value of Z on qubit 0: " << sim.expectation_z(0) << "\n\n";

    benchmark_simulator();
    return 0;
}

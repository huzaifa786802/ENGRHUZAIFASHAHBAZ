import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from scipy import signal
# Step 1: Load and Prepare Audio Signal
file_path = r'c:\Users\Nobel\Downloads\sample.wav'
audio_data, sampling_rate = librosa.load(file_path, sr=None, mono=True)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(audio_data, sr=sampling_rate)
plt.title('Original Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

# Step 2: Filtering - Apply a Low-pass Filter
def apply_lowpass_filter(audio_data, sampling_rate, cutoff_freq):
    nyquist_rate = sampling_rate / 2
    order = 10
    b, a = signal.butter(order, cutoff_freq / nyquist_rate, btype='low')
    filtered_audio = signal.lfilter(b, a, audio_data)
    return filtered_audio

cutoff_frequency = 4000  # Hz
filtered_audio = apply_lowpass_filter(audio_data, sampling_rate, cutoff_frequency)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(filtered_audio, sr=sampling_rate)
plt.title('Filtered Audio Signal (Low-pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

# Step 3: Z-Transform Analysis - Poles and Zeros Plot
def plot_poles_zeros(b, a):
    zeros, poles, _ = signal.tf2zpk(b, a)
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
    plt.axvline(x=0, color='black', linestyle='--', linewidth=0.5)
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
    plt.title('Poles and Zeros Plot')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

b, a = signal.butter(10, cutoff_frequency / (sampling_rate / 2), btype='low')
plot_poles_zeros(b, a)

# Step 4: Fourier Transform of Filtered Signal
def plot_fourier_transform(signal, sampling_rate):
    fft_freq = np.fft.rfftfreq(len(signal), d=1/sampling_rate)
    fft_mag = np.abs(np.fft.rfft(signal))
    plt.figure(figsize=(10, 4))
    plt.plot(fft_freq, fft_mag)
    plt.title('Fourier Transform of Filtered Audio Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_fourier_transform(filtered_audio, sampling_rate)

# Step 5: Inverse Fourier Transform - Reconstruct Time-domain Signal
def reconstruct_signal_from_fft(fft_signal):
    reconstructed_signal = np.fft.irfft(fft_signal)
    return reconstructed_signal

reconstructed_signal = reconstruct_signal_from_fft(np.fft.rfft(filtered_audio))

plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(reconstructed_signal)) / sampling_rate, reconstructed_signal)
plt.title('Reconstructed Signal from Fourier Transform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

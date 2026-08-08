#include <iostream>
#include <cmath>
using namespace std;
class B;

class A {
private:
    int a;

public:
    A(int val) : a(val) {}
    friend class B;
};
class B {
public:
    double divide(const A& objA, int b) {
        return static_cast<double>(objA.a) / b;
    }
    double power(const A& objA, int b) {
        return pow(objA.a, b);
    }
  int multiply(const A& objA, int b) {
        return objA.a * b;
    }
};
int main() {
    A objA(10);
    B objB;
    double result_divide = objB.divide(objA, 5);
    cout << "Division of a and b: " << result_divide << endl;
    double result_power = objB.power(objA, 3);
    cout << "Power of a and b: " << result_power << endl;
    int result_multiply = objB.multiply(objA, 4);
    cout << "Multiplication of a and b: " << result_multiply << endl;
    return 0;
}
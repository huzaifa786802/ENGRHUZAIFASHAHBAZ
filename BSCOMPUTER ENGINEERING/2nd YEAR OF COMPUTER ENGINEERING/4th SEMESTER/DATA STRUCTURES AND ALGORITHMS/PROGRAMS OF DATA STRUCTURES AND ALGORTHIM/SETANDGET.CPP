#include <iostream>
using namespace std;
class A;
class B;
class A {
private:
    int a;
public:
    A(int val) : a(val) {}
  int getA() const {
        return a;
    }
};
class B {
private:
    int b;
public:
    B(int val) : b(val) {}
    int getB() const {
        return b;
    }
};
class Compare {
public:
    friend void compareValues(const A& objA, const B& objB);
};
void compareValues(const A& objA, const B& objB) {
    if (objA.getA() > objB.getB()) {
        cout << "Greater number: " << objA.getA() << " (from class A)" << endl;
    } else if (objB.getB() > objA.getA()) {
        cout << "Greater number: " << objB.getB() << " (from class B)" << endl;
    } else {
        cout << "Numbers are equal: " << objA.getA() << " (from class A) and " << objB.getB() << " (from class B)" << endl;
    }
}
int main() {
    A objA(10);
    B objB(15);
    compareValues(objA, objB);
    return 0;
}
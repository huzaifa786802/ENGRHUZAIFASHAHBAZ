#include <iostream>
using namespace std;
int power(int n, int x) {
if (x == 0) {
return 1;
}
if (x < 0) {
cout << "Power should be positive" << endl;
return 0;
}
return n * power(n, x - 1);
}

int main() {
power(2, -1);
cout << "Power of 2^0: " << power(2, 0) << endl;
cout << "Power of 2^2: " << power(2, 2) << endl;
return 0;
}
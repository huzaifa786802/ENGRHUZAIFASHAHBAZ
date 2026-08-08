#include <iostream>
using namespace std;
template<class T>
T Average(T arr[], int size) {
T total = 0;
for (int i = 0; i < size; i++) {
total += arr[i];
}
return total / size;
}
int main() {
const int intSize = 4, doubleSize = 5, floatSize = 3;
cout << "INTEGER ARRAY: " << endl << endl;
int intArr[intSize];
for (int i = 0; i < intSize; i++) {
cout << "Enter a number: ";
cin >> intArr[i];
}
cout << "Average: " << Average<int>(intArr, intSize) << endl;
cout << endl;
cout << "DOUBLE ARRAY: " << endl << endl;
double doubleArr[doubleSize];
for (int i = 0; i < doubleSize; i++) {
cout << "Enter a number: ";
cin >> doubleArr[i];
}
cout << "Average: " << Average<double>(doubleArr, doubleSize) << endl;
cout << endl;
cout << "FLOAT ARRAY: " << endl << endl;
float floatArr[floatSize];
for (int i = 0; i < floatSize; i++)
 {
cout << "Enter a number: ";

cin >> floatArr[i];
}
cout << "Average: " << Average<float>(floatArr, floatSize) << endl;
cout << endl;
return 0;
}
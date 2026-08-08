#include <iostream>
using namespace std;
void find(int index, int size, int arr[]) {
if (index >= size) {
return;
}
if (index % 2 == 0 || arr[index] % 3 == 0) {
cout << arr[index] << " ";
}
index++;
find(index, size, arr);
}
int main() {
int a[9] = { 11,36,69,43,15,34,67,72,68 };
find(0, 9, a);
return 0;
}
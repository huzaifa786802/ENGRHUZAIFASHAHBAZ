#include <iostream>
using namespace std;
class Swap {
private:
char* val_1;
char* val_2;
char old_v1 = NULL;
char old_v2 = NULL;
void storeVal_1(char val1) {
if (val_1 != NULL) {
delete val_1;
}
val_1 = new char;
*val_1 = val1;
old_v1 = val1;
}
void storeVal_2(char val2) {
if (val_2 != NULL) {
delete val_2;
}
val_2 = new char;
*val_2 = val2;
old_v2 = val2;
}
public:
Swap() {
val_1 = NULL;
val_2 = NULL;
}
void SetValue(char char1) {
storeVal_1(char1);
}
char GetValue() {
return *val_1;
}
void Display() {
cout << "Before swapping: " << endl << endl;
cout << "Value of char 1: " << old_v1 << endl;
cout << "Value of char 2: " << old_v2 << endl << endl;
cout << "After swapping: " << endl << endl;
cout << "Value of char 1: " << *val_1 << endl;
cout << "Value of char 2: " << *val_2 << endl;
}
void SwapValue(char char2) {
storeVal_2(char2);
char *temp = val_1;
val_1 = val_2;
val_2 = temp;
temp = NULL;
}
~Swap() {
val_1 = NULL;
val_2 = NULL;
delete val_1;
delete val_2;
}
};
int main() {
Swap s;
s.SetValue('A');
s.SwapValue('B');
s.Display();
return 0;
}
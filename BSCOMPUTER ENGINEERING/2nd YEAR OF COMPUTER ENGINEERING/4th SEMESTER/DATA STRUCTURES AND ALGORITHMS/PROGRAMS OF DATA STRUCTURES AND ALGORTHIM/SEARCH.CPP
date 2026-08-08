#include <iostream>
#include "LinkedList.cpp"
using namespace std;
template <class T>
void Search(node<T>* n, T data) {
if (n == NULL) {
cout << "Element: " << data << ", not found." << endl;
return;
}
if (n->data == data) {
cout << "Element: " << data << ", found." << endl;
return;
}
Search(n->next, data);
}
int main() {
LinkedList<int> list;
list.IAE(1);
list.IAE(2);
list.IAE(3);
list.IAE(4);
list.IAE(5);
Search(list.Head(), 6);
Search(list.Head(), 2);
}

#include <iostream>
#include "DynamicStack.cpp"
using namespace std;
template <class T>
void RecursivePrint(node<T>* n) {
if (n == NULL) {
return;
}
cout << n->data << " ";
RecursivePrint(n->next);
}
int main() 
{
DynamicStack<int> s;
s.Push(1);
s.Push(2);
s.Push(3);
s.Push(4);
s.Push(5);
RecursivePrint(s.Top());
}
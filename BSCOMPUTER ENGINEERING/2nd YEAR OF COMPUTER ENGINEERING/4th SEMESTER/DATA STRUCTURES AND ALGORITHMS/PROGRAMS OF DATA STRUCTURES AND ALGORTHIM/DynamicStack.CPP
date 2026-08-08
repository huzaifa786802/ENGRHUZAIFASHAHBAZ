#include <iostream>
using namespace std;
template <class T>
struct node {
T data;
node* next;
};
template <class T>
class DynamicStack {
private:
node<T>* top;
public:
DynamicStack() {
top = NULL;
}
DynamicStack(const DynamicStack& obj) {
top = NULL;
if (obj.top == NULL) {
return;
}
node<T>* temp1 = obj.top;
node<T>* temp2 = NULL;
node<T>* ref = NULL;
while (temp1 != NULL) {
node<T>* n = new node<T>;
n->data = temp1->data;
n->next = NULL;
if (temp2 != NULL) {
temp2->next = n;
}
if (ref == NULL) {
ref = n;
}
temp2 = n;
temp1 = temp1->next;
}
top = ref;
}
~DynamicStack() {
if (IsEmpty()) {
return;
}

while (top != NULL) {
Pop();
}
delete top;
}
bool IsEmpty() {
return top == NULL;
}
void Push(T data) {
node<T>* n = new node<T>;
n->data = data;
n->next = NULL;
if (IsEmpty()) {
top = n;
return;
}
n->next = top;
top = n;
}
T Pop() {
if (IsEmpty()) {
cout << "Error: The stack is empty." << endl;
return NULL;
}
node<T>* temp = top->next;
T popped = top->data;
delete top;
top = temp;
return popped;
}
T RetrieveTop() {
if (IsEmpty()) {
cout << "Error: The stack is empty." << endl;
return NULL;
}
return top->data;
}
};
int main() {
DynamicStack<int> s;
s.Push(1);
s.Push(2);
s.Push(3);
s.Push(4);
s.Push(5);
cout << "Retrieve Top: " << s.RetrieveTop() << endl;
cout << "Pop: " << s.Pop() << endl;

s.Push(6);
cout << "Retrieve Top: " << s.RetrieveTop() << endl;
s.Pop();
s.Pop();
s.Pop();
s.Pop();
s.Pop();
cout << "Retrieve Top: ";
s.RetrieveTop();
return 0;
}
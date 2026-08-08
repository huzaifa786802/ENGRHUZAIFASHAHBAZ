#include <iostream>
using namespace std;
struct node {
int data;
node* next;
};
class LinkedList {
private:
node* head;
public:
LinkedList() {
head = NULL;
}
LinkedList(const LinkedList& list) {
head = list.head;
}
~LinkedList() {
if (head != NULL) {
node* current = head;
node* next;
while (current->next != NULL) {
next = current->next;
delete current;
current = next;
}
current = NULL;
delete current;
next = NULL;
delete next;
}
head = NULL;
delete head;
}
// insert at start
void IAS(int val) {
node* n = new node;
n->data = val;
n->next = NULL;
if (head != NULL) {
n->next = head;
}

head = n;
}
// insert at end
void IAE(int val) {
node* n = new node;
n->data = val;
n->next = NULL;
if (head == NULL) {
head = n;
return;
}
node* endNode = head;
while (endNode->next != NULL) {
endNode = endNode->next;
}
endNode->next = n;
}
// insert at position
// get the node before the current one and change its next node
void IAP(int pos, int val) {
if (IsEmpty()) {
cout << "List is empty" << endl;
return;
}
if (pos <= 0) {
cout << "Invalid position" << endl;
return;
}
int i = 1;
node* current = head;
node* previous = head;
while (current != NULL) {
previous = current;
current = current->next;
i++;
if (i == pos) {
break;
}
}
node* n = new node;
n->data = val;
n->next = previous->next;
previous->next = n;
}
// delete at start
void DAS()

{
if (IsEmpty()) {
cout << "List is empty" << endl;
return;
}
node* next = NULL;
if (head->next != NULL) {
next = head->next;
}
head = NULL;
delete head;
// set head to null if next is null or
// set head to next if next is not null
head = next == NULL ? NULL : next;
}
// delete at end
void DAE() {
if (IsEmpty()) {
cout << "List is empty" << endl;
return;
}
node* previousNode = NULL;
node* endNode = head;
while (endNode->next != NULL) {
previousNode = endNode;
endNode = endNode->next;
}
// freeing up the memory
endNode = NULL;
delete endNode;
previousNode->next = NULL;
delete previousNode->next;
}
// delete at position
void DAP(int pos) {
if (IsEmpty()) {
cout << "List is empty" << endl;
return;
}
if (pos <= 0) {
cout << "Invalid position" << endl;
return;
}
int i = 1;
node* current = head;
node* previous = head;
while (current->next != NULL) {
previous = current;

current = current->next;
i++;
if (i == pos) {
break;
}
}
previous->next = current->next;
// freeing up the memory
current->next = NULL;
delete current->next;
current = NULL;
delete current;
}
// traverse / display
void Traverse() {
if (IsEmpty()) {
cout << "List is empty" << endl;
return;
}
node* n = head;
while (n != NULL) {
cout << n->data << " ";
n = n->next;
}
cout << endl;
}
bool IsEmpty() {
return head == NULL;
}
};
int main() {
LinkedList obj; // part 1
LinkedList cpy(obj); // part 2
// part 3
cout << "Part 3: " << (obj.IsEmpty() ? "EMPTY" : "NOT EMPTY") << endl;
// part 4
obj.IAE(1);
obj.IAE(2);
obj.IAE(3);
obj.IAE(4);
obj.IAE(5);
// part 5
cout << "Part 5: " << (obj.IsEmpty() ? "EMPTY" : "NOT EMPTY") << endl;
cout << "Part 6: ";
obj.Traverse(); // part 6
obj.DAS(); // part 7

cout << "Part 8: ";
obj.Traverse(); // part 8
obj.IAS(6); // part 9
cout << "Part 10: ";
obj.Traverse(); // part 10
obj.IAE(9); // part 11
cout << "Part 12: ";
obj.Traverse(); // part 12
obj.DAE(); // part 13
cout << "Part 14: ";
obj.Traverse(); // part 14
obj.DAP(3); // part 15
cout << "Part 16: ";
obj.Traverse(); // part 16
obj.IAP(4, 7); // part 17
cout << "Part 18: ";
obj.Traverse(); // part 18
obj.DAS(); // part 19
cout << "Part 20: ";
obj.Traverse(); // part 20
obj.DAP(2); // part 21
cout << "Part 22: ";
obj.Traverse(); // part 22
obj.DAS(); // part 23
obj.DAS(); // part 24
obj.DAS(); // part 25
cout << "Part 26: ";
obj.Traverse(); // part 26
}
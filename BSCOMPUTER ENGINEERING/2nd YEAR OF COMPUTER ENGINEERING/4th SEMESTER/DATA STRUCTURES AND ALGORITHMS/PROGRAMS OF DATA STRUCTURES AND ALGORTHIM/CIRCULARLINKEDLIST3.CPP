#include <iostream>
using namespace std;
template <class T>
struct node {
T data;
node* next;
};
template <class T>
class CircularLinkedList {
private:
node<T>* tail;
public:
// default constructor
CircularLinkedList() {
tail = NULL;
}
// copy constructor
CircularLinkedList(const CircularLinkedList& obj) {
tail = NULL;
if (obj.tail == NULL) {
return;
}
// there is only one node present in obj
if (obj.tail == obj.tail->next) {
IAS(obj.tail->data);
return;
}
int i = 1;
node<T>* objTail = obj.tail;
do {
IAP(i++, objTail->data);
objTail = objTail->next;
} while (objTail != obj.tail);
}
// destructor
~CircularLinkedList() {
if (tail == NULL) {
return;
}
node<T>* current = tail->next;
node<T>* next;
do {
next = current->next;
delete current;

current = next;
} while (current != tail);
delete current;
}
// check if the linked list is empty
bool IsEmpty() {
return tail == NULL;
}
// insert at start
void IAS(T data) {
node<T>* n = new node<T>;
n->data = data;
if (!IsEmpty()) {
n->next = tail->next;
tail->next = n;
return;
}
n->next = n;
tail = n;
}
// insert at end
void IAE(T data) {
node<T>* n = new node<T>;
n->data = data;
if (IsEmpty()) {
IAS(data);
return;
}
n->next = tail->next;
tail->next = n;
tail = n;
}
// insert at any position
void IAP(int pos, T data) {
if (pos <= 0) {
cout << "Invalid position" << endl;
return;
}
// insert the data at the start of the node if the node is empty
if (IsEmpty()) {
IAS(data);
return;
}
bool found = false;
int i = 1;
node<T>* current = tail->next;
node<T>* previous = tail;

do {
previous = current;
current = current->next;
i++;
if (i == pos) {
found = true;
break;
}
} while (current != tail->next);
// the given pos was not found and so insert the data at the end of the
// list
if (!found) {
// cout << "Error: Given position: " << pos << " was not found in
// the list. Insertion is imposible!" << endl;
IAE(data);
return;
}
node<T>* n = new node<T>;
n->data = data;
n->next = current;
previous->next = n;
}
// delete at start
void DAS() {
if (IsEmpty()) {
cout << "The list is empty. There is nothing to delete." << endl;
return;
}
// there is only one value in the list
if (tail == tail->next) {
delete tail;
tail = NULL;
return;
}
node<T>* n = tail->next;
tail->next = n->next;
delete n;
}
// delete at end
void DAE() {
if (IsEmpty()) {
cout << "The list is empty. There is nothing to delete." << endl;
return;
}
// there is only one value in the list so let DAS() handle it
if (tail == tail->next) {
DAS();
return;
}

node<T>* previous = tail;
while (previous->next != tail) {
previous = previous->next;
}
previous->next = tail->next;
delete tail;
tail = previous;
}
// delete at position
void DAP(int pos) {
if (IsEmpty()) {
cout << "The list is empty. There is nothing to delete." << endl;
return;
}
if (pos == 1) {
DAS();
return;
}
// there is only one value in the list so let DAS() handle it
if (tail == tail->next) {
// check if the pos was greater than one in case of only one
// value set, error out
if (pos > 1) {
cout << "Error: Invalid position: " << pos << ". There is no value set at this position." << endl;
return;
}
DAS();
return;
}
bool found = false;
int i = 1;
node<T>* current = tail->next;
node<T>* previous = tail;
do {
previous = current;
current = current->next;
i++;
if (i == pos) {
found = true;
break;
}
} while (current != tail);
// the node to delete was not found and so delete the end node
if (!found) {
// cout << "Error: Given position: " << pos << " was not found in
// the list. Deletion is imposible!" << endl;
DAE();
return;
}

previous->next = current->next;
// the node to delete was a pointer to tail, i could call the delete at
// end function but that would create an unnecessary overhead since it
// would have to again traverse throughout the entire array, setting
// tail equals to previous node removes the overhead
if (current == tail) {
tail = previous;
}
delete current;
}
// traverse the list
void Traverse() {
if (IsEmpty()) {
cout << "The list is empty. There is nothing to traverse." <<
endl;
return;
}
node<T>* temp = tail->next;
do {
cout << temp->data << " ";
temp = temp->next;
} while (temp != tail->next);
cout << endl;
}
};
int main() {
CircularLinkedList<int> myList; // part 1
CircularLinkedList<int> copyList(myList); // part 2
cout << "Part 3) List empty: " << (myList.IsEmpty() ? "YES" : "NO") << endl; //part 3
// part 4
myList.IAE(1);
myList.IAE(2);
myList.IAE(3);
myList.IAE(4);
myList.IAE(5);
cout << "Part 5) List empty: " << (myList.IsEmpty() ? "YES" : "NO") << endl; //part 5
// part 6
cout << "Part 6) Traverse: ";
myList.Traverse();
myList.DAS(); // part 7
// part 8
cout << "Part 8) Traverse: ";
myList.Traverse();
myList.IAS(6); // part 9
// part 10

cout << "Part 10) Traverse: ";
myList.Traverse();
myList.IAE(9); // part 11
// part 12
cout << "Part 12) Traverse: ";
myList.Traverse();
myList.DAE(); // part 13
// part 14
cout << "Part 14) Traverse: ";
myList.Traverse();
myList.DAP(3); // part 15
// part 16
cout << "Part 16) Traverse: ";
myList.Traverse();
myList.IAP(4, 7); // part 17
// part 18
cout << "Part 18) Traverse: ";
myList.Traverse();
CircularLinkedList<float> myList2; // part 19
// part 20
myList2.IAE(1.5);
myList2.IAE(2.5);
myList2.IAE(3.5);
myList2.IAE(4.5);
myList2.IAE(5.5);
myList2.DAP(2); // part 21
// part 22
cout << "Part 22) Traverse: ";
myList2.Traverse();
myList2.IAS(5.5); // part 23
myList2.IAE(6.5); // part 24
myList2.IAP(5, 7.7); // part 25
// part 26
cout << "Part 26) Traverse: ";
myList2.Traverse();
return 0;
}
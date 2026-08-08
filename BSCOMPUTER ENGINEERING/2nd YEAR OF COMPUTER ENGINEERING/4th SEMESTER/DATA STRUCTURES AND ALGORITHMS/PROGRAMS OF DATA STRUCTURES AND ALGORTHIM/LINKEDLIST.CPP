#include <iostream>
using namespace std;
class Node {
public:
    int data;
    Node* next;
    Node(int val) {
        data = val;
        next = nullptr;
    }
};
class LinkedList {
private:
    Node* head;
public:
    LinkedList() {
        head = nullptr;
    }
    void insert(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr || val < head->data) {
            newNode->next = head;
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr && temp->next->data < val) {
            temp = temp->next;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
    void deleteNode(int val) {
        if (head == nullptr)
            return;
        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr && temp->next->data != val) {
            temp = temp->next;
        }
        if (temp->next != nullptr) {
            Node* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
        }
    }
  void display() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};
int main() {
    LinkedList myList;
    myList.insert(5);
    myList.insert(2);
    myList.insert(8);
    myList.insert(4);
    myList.insert(7);
    cout << "Linked List after insertion: ";
    myList.display();
    myList.deleteNode(4);
    cout << "Linked List after deletion: ";
    myList.display();
    return 0;
}
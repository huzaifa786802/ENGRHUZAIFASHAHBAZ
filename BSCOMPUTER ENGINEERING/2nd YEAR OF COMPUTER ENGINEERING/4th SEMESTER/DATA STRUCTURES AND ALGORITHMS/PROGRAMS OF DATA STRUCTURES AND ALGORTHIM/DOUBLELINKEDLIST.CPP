#include <iostream>
using namespace std;
class Node {
public:
    int data;
    Node* prev;
    Node* next;
    Node(int val) {
        data = val;
        prev = nullptr;
        next = nullptr;
    }
};
class DoublyLinkedList {
private:
    Node* head;
    Node* tail;
public:
    DoublyLinkedList() {
        head = nullptr;
        tail = nullptr;
    }
    void insert(int val) {
        Node* newNode = new Node(val);
   if (head == nullptr || val <= head->data) {
            newNode->next = head;
            if (head)
                head->prev = newNode;
            head = newNode;
            if (tail == nullptr)
                tail = head;
        } else {
            Node* curr = head;
            while (curr->next != nullptr && curr->next->data < val) {
                curr = curr->next;
            }
            newNode->next = curr->next;
            if (curr->next)
                curr->next->prev = newNode;
            curr->next = newNode;
            newNode->prev = curr;
            if (newNode->next == nullptr)
                tail = newNode;
        }
    }
    void deleteNode(int val) {
        if (head == nullptr)
            return;
        Node* temp = head;
        if (head->data == val) {
            head = head->next;
            if (head)
                head->prev = nullptr;
            delete temp;
            return;
        }
        while (temp != nullptr && temp->data != val) {
            temp = temp->next;
        }
        if (temp == nullptr)
            return;
        if (temp == tail) {
            tail = tail->prev;
            if (tail)
                tail->next = nullptr;
            delete temp;
            return;
        }
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        delete temp;
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
    DoublyLinkedList myList;
    myList.insert(5);
    myList.insert(3);
    myList.insert(8);
    myList.insert(1);
    cout << "Linked List after insertion: ";
    myList.display();
    myList.deleteNode(3);
    cout << "Linked List after deletion: ";
    myList.display();
    return 0;
}
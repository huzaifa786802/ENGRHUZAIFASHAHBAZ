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
class CircularDoublyLinkedList {
private:
    Node* head;
public:
    CircularDoublyLinkedList() {
        head = nullptr;
    }
    void insert(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr || val <= head->data) {
            newNode->next = head;
            if (head)
                head->prev = newNode;
            head = newNode;
            head->prev = head; 
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
                newNode->next = head; 
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
        if (temp->data == head->data)
            head = temp->next;

        temp->prev->next = temp->next;
        if (temp->next)
            temp->next->prev = temp->prev;
        delete temp;
    }
    void display() {
        if (head == nullptr) {
            cout << "List is empty" << endl;
            return;
        }
        Node* temp = head;
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != head);
        cout << endl;
    }
};
int main() {
    CircularDoublyLinkedList myList;
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
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
class SortedCircularLinkedList {
private:
    Node* head;
public:
    SortedCircularLinkedList() {
        head = nullptr;
    }
    void insert(int val) {
        Node* newNode = new Node(val);
   if (head == nullptr || val <= head->data) {
            newNode->next = head ? head : newNode; 
            head = newNode;
        } else {
            Node* curr = head;
            while (curr->next != head && curr->next->data < val) {
                curr = curr->next;
            }
            newNode->next = curr->next;
            curr->next = newNode;
        }
    }
    void deleteNode(int val) {
        if (head == nullptr)
            return;
        Node* temp = head;
        Node* prev = nullptr;
        while (temp->data != val) {
            if (temp->next == head) {
                cout << "Value not found in the list" << endl;
                return;
            }
            prev = temp;
            temp = temp->next;
        }
   if (temp == head) {
            if (temp->next == head) {
                delete temp;
                head = nullptr;
            } else {
                prev = head;
                while (prev->next != head)
                    prev = prev->next;
                prev->next = head->next;
                delete head;
                head = prev->next;
            }
        } else {
            prev->next = temp->next;
            delete temp;
        }
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
    SortedCircularLinkedList myList;
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
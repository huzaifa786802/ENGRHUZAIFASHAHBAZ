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
class SortedSinglyLinkedList {
private:
    Node* head;    
public:
    SortedSinglyLinkedList() {
        head = nullptr;
    }
    void insert(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr || val < head->data) {
            newNode->next = head;
            head = newNode;
        } 
        else {
            Node* curr = head;
            while (curr->next != nullptr && curr->next->data < val) {
                curr = curr->next;
            }
            newNode->next = curr->next;
            curr->next = newNode;
        }
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
        Node* curr = head;
        while (curr->next != nullptr && curr->next->data != val) {
            curr = curr->next;
        }
        if (curr->next != nullptr) {
            Node* temp = curr->next;
            curr->next = curr->next->next;
            delete temp;
        }
    }
  void display() {
        Node* curr = head;
        while (curr != nullptr) {
            cout << curr->data << " ";
            curr = curr->next;
        }
        cout << endl;
    }
};
int main() {
    SortedSinglyLinkedList myList;
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
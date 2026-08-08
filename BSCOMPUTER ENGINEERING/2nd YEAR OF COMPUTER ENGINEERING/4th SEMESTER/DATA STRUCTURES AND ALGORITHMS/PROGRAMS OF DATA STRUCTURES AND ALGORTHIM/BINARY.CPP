#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};
void insert(Node*& head, int value) {
    if (head == nullptr) {
        head = new Node(value);
    } else {
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = new Node(value);
    }
}
void display(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}
Node* findMiddle(Node* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    Node* slow = head;
    Node* fast = head->next;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
Node* binarySearch(Node* head, int key) {
    Node* left = head;
    Node* right = nullptr;
    while (head->next != nullptr) {
        head = head->next;
    }
    right = head;

    while (left != right) {
        Node* mid = findMiddle(left);
        if (mid->data == key) {
            return mid;
        } else if (mid->data < key) {
            left = mid->next;
        } else {
            right = mid;
        }
    }
    return nullptr;
}
int main() {
    Node* head = nullptr;
    insert(head, 10);
    insert(head, 20);
    insert(head, 30);
    insert(head, 40);
    insert(head, 50);
    cout << "Linked List: ";
    display(head);
    int key;
    cout << "Enter the element to search: ";
    cin >> key;
    Node* result = binarySearch(head, key);
    if (result != nullptr) {
        cout << "Element found at address: " << result << endl;
    } else {
        cout << "Element not found." << endl;
    }
    return 0;
}
#include <iostream>
#define size 5
using namespace std;
template <class T>
class StaticQueue {
private:
int front;
int back;
T queue[size];
public:
StaticQueue() {
front = 0;
back = 0;
}
StaticQueue(const StaticQueue& obj) {
front = obj.front;
back = obj.back;
if (front == back) {
return;
}
for (int i = front; i < back; i++) {
queue[i] = obj.queue[i];
}
}
~StaticQueue() {
if (IsEmpty()) {
return;
}
front = 0;
back = 0;
}
bool IsEmpty() {
return back == front;
}
void Enqueue(T data) {
if (back == size) {
cout << "Error: Queue Overflow. Queue is full." << endl;
return;
}
queue[back++] = data;
}
T Dequeue() {
if (IsEmpty()) {
cout << "Error: Queue Underflow. Queue is empty." << endl;

return 0;
}
T value = queue[front];
for (int i = front + 1; i < back; i++) {
queue[i - 1] = queue[i];
}
queue[--back] = 0; // remove value from rear and decrement its
return value;
}
void Display() {
if (IsEmpty()) {
cout << "Error: Queue is empty." << endl;
return;
}
cout << queue[front] << endl;
}
};
int main() {
StaticQueue<int> queue; // part 1
// part 2
queue.Enqueue(1);
queue.Enqueue(2);
queue.Enqueue(3);
queue.Enqueue(4);
queue.Enqueue(5);
cout << "Part 3: " << queue.Dequeue() << endl; // part 3
queue.Enqueue(6); // part 4
cout << "Part 5: " << queue.Dequeue() << endl; // part 5
cout << "Part 6: " << queue.Dequeue() << endl; // part 6
cout << "Part 7: " << queue.Dequeue() << endl; // part 7
cout << "Part 8: "; queue.Display(); // part 8
cout << "Part 9: " << queue.Dequeue() << endl; // part 9
cout << "Part 10: " << queue.Dequeue() << endl; // part 10
queue.Enqueue(7); // part 11
queue.Enqueue(8); // part 12
cout << "Part 13: "; queue.Display(); // part 13
return 0;
}
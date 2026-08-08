 #include <iostream>

 using namespace std;

 class IntDynamicPointer {

 private:
	int* ptr;

 public:

	IntDynamicPointer() {
		ptr = NULL;
	}

	void AllocMemory() {
		if (ptr != NULL) {
			delete ptr;
		}

		ptr = new int;
	}

	void setValue(int val) {
		AllocMemory();
		*ptr = val;
	}

	int getValue() {
		return *ptr;
	}

	~IntDynamicPointer() {
		ptr = NULL;
		delete ptr;
	}
 };

 int main() {

	int b = 10;

	IntDynamicPointer p1;
	p1.setValue(b);
	cout << "P1: " << p1.getValue() << endl;

	b = 11;

	IntDynamicPointer p2;
	p2.setValue(b);
	cout << "P2: " << p2.getValue() << endl;

	return 0;
 }

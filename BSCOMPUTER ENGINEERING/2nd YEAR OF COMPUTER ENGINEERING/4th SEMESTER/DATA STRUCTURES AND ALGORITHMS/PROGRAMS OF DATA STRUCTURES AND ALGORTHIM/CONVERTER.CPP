#include <iostream>
using namespace std;
class Convertor 
{ 
	private: 
	int* ptr;
void AllocMemory() 
{ 
	if (ptr != NULL) 
	{ 
		delete ptr; 
	} 
	ptr = new int;
}
public:
Convertor() 
{ 
	ptr = NULL;
}
void SetValue(int val) 
{  
	AllocMemory(); 
	*ptr = val;
}
float Convert()  
{ 
	*ptr *= 1000; 
	return (float) *ptr;
}
float Convert(int val) 
{ 
	SetValue(val); 
	return Convert();
}
void Display() 
{ 
	int weightInKg = *ptr / 1000; 
	cout << weightInKg << "kg is equivalent to: " << *ptr << "g" << endl;
}
~Convertor() 
{ 
	ptr = NULL; 
	delete ptr;
}
};
int main() 
{ 
	Convertor c; 
	c.SetValue(20); 
	c.Convert(); 
	c.Display(); 
	c.Convert(40); 
	c.Display(); 
	return 0;
}
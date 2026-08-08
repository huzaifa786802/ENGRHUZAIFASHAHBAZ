#include<iostream>
#include<conio.h>
using namespace std;
class square
{
private:
	double side;
public:
	square(double side)
	{
		this->side=side;

	}
	double getside()
	{
		return side;
	}
	double getarea()
	{
		return side*side;
	}
	double getperimeter()
	{
		return 4*side;
	}
};
int main()
{
	const double side=10.5;
	square s(side);
	cout<<"Enter side of square is:"<<s.getside()<<endl;
	cout<<"Area:"<<s.getarea()<<endl
	cout<<"Perimeter:"<<s.getperimeter()<<endl;
	getch();
	return 0;
}
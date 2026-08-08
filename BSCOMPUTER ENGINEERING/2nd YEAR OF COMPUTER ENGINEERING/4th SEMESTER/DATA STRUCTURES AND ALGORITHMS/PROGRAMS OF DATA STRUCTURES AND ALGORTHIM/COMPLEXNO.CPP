#include<iostream>
#include<cmath>
#include<conio.h>
#include<sstream>
using namespace std;
class ComplexNo
{
private:
	double real;
	double imaginary;
public:
	ComplexNo()
	{
		real=0;
		imaginary=0;
	}
	ComplexNo(double r,double i)
	{
		real=r;
		imaginary=i;
	}
	double getReal()
	{
		return real;
	}
	double getImaginary()
	{
		return imaginary
	}
	string Display()
	{
		stringstream ss;
		ss<<real<<"+"<<imaginary<<"i";
		return ss.str();
	}
	double Magnitude()
	{
		return sqrt(pow(real,2)+low(imaginary,2));
	}
	string Sum(ComplexNo)
	{
		double sum_real=real+c.getReal();
		double sum_img=imaginary+c.getImaginary();
		return Display(sum_real,sum_img);
	} 
};
int main()
{
	double r1,i1,r2,i2;
	cout<<"complex number 1:"<<endl;
	cout<<"Enter the real part:";
	cin>>r1;
	cout<<"Please enter the imaginary part:"<<endl;
	cin>>i1;
	cout<<endl;
	cout<<"complex number 2:"<<endl;
	cout<<"Enter the real part:";
	cin>>r2;
	cout<<"Please enter the imaginary part:"<<endl;
	cin>>i2;
	cout<<endl;
	ComplexNo c1(r1,i1);
	ComplexNo c2(r2,i2);
	cout << "Complex Number 1: " << c1.Display() << endl;
    cout << "Complex Number 2: " << c2.Display() << endl;
    cout << "Magnitude of complex number 1: " << c1.Magnitude() << endl;
    cout << "Magnitude of complex number 2: " << c2.Magnitude() << endl;
    cout << "(" << c1.Display() << ") + (" << c2.Display() << ") = " << c1.Sum(c2)<< endl;
   getch();
	return 0;
}
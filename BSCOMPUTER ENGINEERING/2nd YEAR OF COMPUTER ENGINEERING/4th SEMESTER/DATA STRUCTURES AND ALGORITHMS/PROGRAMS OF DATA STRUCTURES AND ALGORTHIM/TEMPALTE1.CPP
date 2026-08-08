#include<iostream>
using namespace std;
template<class T>
T * ReverseArray(T * arr, int size)
{
	T* temp =new T[size];
	for(int i=0; i<size;i++)
	{
		temp[i]=arr[i];
	}
	for(int i=size-1,j=0; i>-1;i--,j++)
	{
		arr[j]=temp[i];
	}
	delete[] temp;
	return arr;
}
int main()
{
	const int s=5;
	int arr[s];
	for(int i=0;i<s;i++)
	{
		cout<<"Enter a number:";
		cin>>arr[i];
	}
	cout<<endl;
	cout<<"Original array:";
	for(int i=0;i<s;i++)
	{
		cout<<arr[i]<<"";
	}
	cout<<endl;
	cout<<"Reversed array:";
	for(int i=0;i<s;i++)
	{
		cout<<arr[i]<<"";
	}
	cout<<endl;
	return 0;
}
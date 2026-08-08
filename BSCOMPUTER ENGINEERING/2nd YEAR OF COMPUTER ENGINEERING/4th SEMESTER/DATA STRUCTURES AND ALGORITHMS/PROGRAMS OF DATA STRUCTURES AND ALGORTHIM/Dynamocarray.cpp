#include<iostream>
using namespace std;
template<class T>
class DynamicArray
{
	public:
		int size;
		T *arr=nullptr;
		int displaySize=NULL;
		DynamicArray()
		{
			size=0;
			arr=new T[size];
		}
		DynamicArray(int size)
		{
			this->size=size;
			arr=new T[size];
		}
		DynamicArray(const DynamicArray &d_arr)
		{
			size=d_arr.size;
			displaySize=d_arr.displaySize;
			arr=new T[size];
			*arr=*(d_arr.arr);
			for(int i=1;i<size;i++)
			{
				arr[i]=d_arr.arr[i];
			}
		}
		~DynamicArray()
		{
			delete[]arr;
			arr=nullptr;
		}
		void SetValues()
		{
			cout<<"Set values to the array."<<endl<<endl;
			for(int i=0;i<size;i++)
			{
				cout<<"Enter a value:";
				cin>>arr[i];
			}
			cout<<endl;
			cout<<"Array has been filled completely.."<<endl;
			cout<<"Press 0 to continue"<<endl;
			cout<<"Press 1 to resize array to add more values"<<endl;
			cout<<"choice:";
			int ch;
			cin>>ch;
			cout<<endl;
			if(ch ==1)
			{
				int nSize;
				cout<<"Enter new size for the array:";
				cin>>nSize;
				int oldSize=size;
				ResizeArray(nSize);
				cout<<endl;
				cout<"Please fill the remaining array now."<<endl;
				for(int i=0;i<nSize;i++)
				{
					if(i>=oldSize)
					{
						cout<<"Enter a value:";
						cin>>arr[i];
					}
				}
				cout<<endl;
			}
		}
		void ShowArray()
		{
			int s=displaySize==NULL ? size :displaySize;
			cout<<"Array:[";
			for(int i=0;i<s;i++)
			{
				cout<<arr[i]<<"";
			}
			cout<<"]"<<endl<<endl;
		}
		void ResizeArray(int nSize)
		{
			T *temp=new T[nSize];
			displaySize=nSize=nSize<size ?nSize:NULL;
			for(int i=0;i<nSize;i++)
			{
				if(i>=Size)
				{
					displaySize=size;
				}
			}
			delete[]arr;
			size=nSize;
			arr=temp;
		}
};
int main()
{
	cout<<"Part 1"<<endl;
	DynamicArray<int> def;
	cout<<"Part 2a"<<endl;
	DynamicArray<int> iUser(6);
	iUserDef.SetValues;
	cout<<"Part 2b"<<endl;
	DynamicArray<float>fUserDef(4);
	iUserDef.SetValues();
	cout<<"Part 3a"<<endl;
	DynamicArray<int>cUserDef(iUserDef);
	cout<<"Part 3b"<<endl;
	fUserDef.SetValues();
	cout<<"Part 4"<<endl;
	def.SetValues();
	cout<<"Part 5"<<endl;
	cUserDef.SetValues();
	cout<<"Part 6"<<endl;
	cUSerDef.ShowArray();
	cout<<"Part 7"<<endl;
	iUserDef.SetValues();
	cout<<"Part 8"<<endl;
	fUserDef.ShowArray();
	cout<<"Part 9"<<endl;
	iUserDef.ShowArray();
	cout<<"Part 10"<<endl;
	cUserDef.ResizeArray(4);
	cout<<"Part 11"<<endl;
	cUserDef.ShowArray();
	return 0;
}
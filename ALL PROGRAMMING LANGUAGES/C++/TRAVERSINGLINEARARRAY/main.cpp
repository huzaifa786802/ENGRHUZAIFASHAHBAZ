#include<iostream>
using  namespace std;
class lineararray
{
private:
    int LA[5];
    int N;
    int C;
    int length;
    int location;
    int item;
public:
    lineararray()
    {
        cout<<"Enter the size of array:"<<endl;
        cin>>N;
        for (int i=0;i<=N;i++)
        {
            LA[i]=0;
        }
        C=0;
    }
    void display()
    {
        int k=0;
        while (k<N)
        {
            cout<<LA[k]<<endl;
            k++;
        }
    }
    void insertion(int item,int loc)
    {
        if(C==0)
        {
            cout<<"full"<<endl;
        }
        else if(LA[loc]==0)
        {
            LA[loc]=item;
        }
        else
        {
            int j=10;
            while (j<=loc)
            {
                LA[j-1]=LA[j-2];
                j--;
            }
            LA[loc]=item;
        }
    }
};
int main()
{
    lineararray l;
    l.insertion(5,3);
    l.display();
    cout<<endl;
    l.insertion(7,3);
    l.display();
    return 0;
}
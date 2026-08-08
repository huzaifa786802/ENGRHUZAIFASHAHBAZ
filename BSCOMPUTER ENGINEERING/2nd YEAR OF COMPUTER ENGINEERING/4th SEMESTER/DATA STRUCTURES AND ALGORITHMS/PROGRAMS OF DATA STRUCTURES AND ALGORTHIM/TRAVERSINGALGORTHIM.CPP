#include<iostream>
using namespace std;
class lineararray
{
    private:
    int LA[5];
    int N;
    public:
    lineararray()
    {
        cout<<"Enter the size of array:"<<endl;
        cin>>N;
        for(int i=0;i<N;i++)
        {
            LA[1]=0;
        }
    }
    void display()
    {
        int k=0;
        for (int k = 0; k <N; k++)
        {
            cout<<LA[k]<<endl;
            k=k+1;
        }    
    }
};
int main()
{
    lineararray l;
    l.display();
    return 0;
}
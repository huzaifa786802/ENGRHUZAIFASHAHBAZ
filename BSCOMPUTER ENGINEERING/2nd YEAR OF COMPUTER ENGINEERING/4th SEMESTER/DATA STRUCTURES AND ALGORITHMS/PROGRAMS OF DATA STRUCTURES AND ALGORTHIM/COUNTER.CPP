#include<iostream>
using namespace std;
class COUNTER
{
private:
    int pos;
public:
    static int count;
    COUNTER()
    {
        pos=++count;
    }
    int Mypos()
    {
        return pos;
    }
    void DisplayTotal()
    {
        cout<<"Total count:"<<count<<endl;
    }
};    
int COUNTER::count=0;
int main()
{
    COUNTER a;
    COUNTER b;
    COUNTER c;
    a.DisplayTotal();
    cout<<endl;
    cout<<"Pos of A:"<<a.Mypos()<<endl;
    cout<<"Pos of B:"<<b.Mypos()<<endl;
    cout<<"Pos of C:"<<c.Mypos()<<endl;
    return 0;
}
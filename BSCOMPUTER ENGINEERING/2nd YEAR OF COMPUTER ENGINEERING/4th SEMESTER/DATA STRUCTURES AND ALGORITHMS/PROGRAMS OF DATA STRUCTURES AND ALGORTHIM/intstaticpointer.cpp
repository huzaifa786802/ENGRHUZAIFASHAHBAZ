#include<iostream>
using namespace std;
class intstaticpointer
{
private:
    int*ptr;
public:
    intstaticpointer()
    {
        ptr=NULL;
    }
    void setValue(int&value)
    {
        ptr=&value;
    }
    int getValue()
    {
        return *ptr;
    }
    ~intstaticpointer()
    {
        ptr=NULL;
    }
};
int main()
{
    int b=10;
    intstaticpointer p1;
    p1.setValue(b);
    cout<<"P1:"<<p1.getValue()<<endl;
    b=11;
    intstaticpointer p2;
    p2.setValue(b);
    cout<<"P2:"<<p2.getValue()<<endl;
    b=12;
    intstaticpointer p3;
    p3.setValue(b);
    cout<<"P3:"<<p3.getValue<<endl;
    return 0;
}
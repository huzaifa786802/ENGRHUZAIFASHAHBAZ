#include<iostream>
#include<cstdlib.h>
using namespace std;
int main()
{
    float sensor;
    for(int i=0; i<10;i++)
    {
        sensor=(rand()%50);
        cout<<sensor<<endl;
        if(sensor<=20)
        {
            cout<<"Turn the AC off"<<endl;
        }
        else
        {
            cout<<"Turn the AC on"<<endl;
        }
    }
    return 0;
}
#include<iostream>
using namespace std;
int main()
{
    int x,y;
    int*p,*q;
    x=2;
    y=8;
    p=&x;
    q=&y;
    cout<<&x<<"-"<<x<<endl;//part1
    cout<<p<<"-"<<*p<<endl;//part2
    cout<<&y<<"-"<<y<<endl;//part3
    cout<<q<<"-"<<*q<<endl;//part4
    cout<<&p<<"-"<<p<<endl;//part5
    cout<<&q<<"-"<<q<<endl;//part6
    return 0;
}
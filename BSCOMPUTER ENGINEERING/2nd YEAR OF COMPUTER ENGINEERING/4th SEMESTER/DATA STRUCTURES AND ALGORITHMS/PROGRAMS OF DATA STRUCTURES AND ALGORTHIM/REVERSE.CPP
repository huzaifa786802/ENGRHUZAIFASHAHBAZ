#include<iostream>
#include"DynamicStack.CPP";
#include"LinkedList.CPP";
using namespace std;
template<class T>
void ReversePrint(node<T>*n)
{
    if (n==NULL)
    {
        return;
    }
    DynamicStack<T> stack;
    while (n!=NULL)
    {
        stack.push(n->data);
        n = n->next;
    }
    while (!stack.empty())
    {
        cout<<"stack.Pop()"<<"";
    }
    cout<<endl;
}
int main()
{
    list.IAE(1);
    list.IAE(2);
    list.IAE(3);
    list.IAE(4);
    list.IAE(5);
    list.IAE(6);
    list.IAE(7);
    ReversePrint(list.Head);
    return 0;
}
#include<iostream>
#include"LinkedList.cpp";
using namespace std;
template<class T>
void AlternativeNodes(node<T> *n,bool is_even,int index=1)
{
    if (n==NULL)
    {
        cout<<endl;
        return;
    }
    if ((is_even && index%2==0) || (is_even && index%2!=0))
    {
        cout<<n->data<<"";
    }
    AlternativeNodes(n->next,is_even,index+1);
}
int main()
{
    LinkedList<int> list;
    list.IAE(1);
    list.IAE(2);
    list.IAE(3);
    list.IAE(4);
    list.IAE(5);
    list.IAE(6);
    list.IAE(7);
    cout<<"Even:"<<AlternativeNodes(list.Head(),true);
    cout<<"Odd:"<<AlternativeNodes(list.Head(),true);
    return 0;
}
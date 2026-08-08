#include<iostream>
#include"LinkedList.cpp";
template <class T>
void fun(node<T>*head)
{
    if (head==NULL)
    {
        return;
    }
    head=head->next;
    cout<<head->data<<endl;
    if (head->next==NULL)
    {
        fun(head->next);
    }
    cout<<head->data<<endl;
}
int main()
{
    LinkedList<int> list;
    list.IAE(5);
    list.IAE(4);
    list.IAE(3);
    list.IAE(2);
    list.IAE(1);
    list.IAE(0);
    fun(list.Head);
    return 0;    
}
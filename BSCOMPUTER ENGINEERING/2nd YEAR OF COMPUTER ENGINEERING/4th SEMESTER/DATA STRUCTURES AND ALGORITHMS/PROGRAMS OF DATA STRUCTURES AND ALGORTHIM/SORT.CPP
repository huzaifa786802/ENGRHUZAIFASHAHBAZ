#include<iostream>
#include"DynamicStack.CPP";
template<class T>
void SortQueue(node<T>*current,node<T>*next)
{
    if (current==NULL || next==NULL)
    {
        return;
    }
    if (current->data<next->data)
    {
        T temp=current->data;
        current->data=next->data;
    }
    
}
#include<iostream>
#define size 5;
using namespace std;
template<class T>
class STATICSTACK
{
private:
    int top;
    T stack[size];
public:
    STATICSTACK()
    {
        top=-1;
    }
    STATICSTACK(const STATICSTACK& obj)
    {
        top=obj.top;
        if (obj.IsEmpty())
        {
            return;
        }
        for (int i = 0; i < obj.top; i++)
        {
            stack[i] = obj.stack[i];   
        }
    }
    ~STATICSTACK()
    {
        top=-1;
    }
    bool IsEmpty()
    {
        return top==-1;
    }
    void Push(T value)
    {
        top++;
        if (top>=size)
        {
            top--;
            cout<<"Error:The stack is full."<<endl;
            return;
        }
        stack[top] = value;
    }
    T Pop()
    {
        if (IsEmpty())
        {
            cout<<"Error:The stack is empty."<<endl;
            return NULL;
        }
        T value = stack[top];
        stack[top] = value;
        top--;
        return value;
    }
    T RetrieveTop()
    {
        if (IsEmpty())
        {
            cout<<"Error:The stack is empty."<<endl;
            return NULL;
        }
        return stack[top];
    }
};       
int main()
{
    STATICSTACK<int> s;
    s.Push(1);
    s.Push(2);
    s.Push(3);
    s.Push(4);
    s.Push(5);
    cout<<"Retrieve Top:"<<s.RetrieveTop()<<endl;
    cout<<"Pop: "<<s.Pop()<<endl;
    s.Push(6);
    cout<<"Retrieve Top:"<<s.RetrieveTop()<<endl;
    s.Pop();
    s.Pop();
    s.Pop();
    s.Pop();
    s.Pop();
    cout<<"Retrieve Top:";
    s.RetrieveTop();
    return 0;
}         
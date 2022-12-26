#include <iostream>
#include<string.h>
#define MAX 50
using namespace std;

class stack
{
private:
    char stk[MAX];
    int top,Top;
    string str;

public:
    stack()
    {
        top = -1;
        Top=-1;
        str = " ";
    }
    bool isFull()
    {
        if (top == (MAX - 1))
        {
            return true;
        }
        else
        {
            return false;
        }
    };
    bool isEmpty()
    {
        if (top == -1)
        {
            return true;
        }
        else
        {
            return false;
        }
    };
    void push(char a)
    {
        if (isFull())
        {
            cout<< "\nStack is full" << endl;
        }
        else
        {
            top++;
            stk[top]=a;
        }
    };
    void pop()
    {
        if(isEmpty())
            cout<<"\nStack is already Empty"<<endl;
        else
        {
            char a;
            a=stk[top];
            top--;
        }
    }
    void revstk()
    {
        int flag=0;
        char revstk[MAX];
        int t=top;
        while(t!=-1)
        {
            revstk[Top++]=stk[t--];
        }

        t=top;
        while(t!=-1)
        {
            if(stk[t--]==revstk[Top--])
            {
                flag+=1;
            }
        }
        if(flag==top)
        {
            cout<<"\nString you entered is Palindrome"<<endl;
        }
        else
        {
            cout<<"\nString you entered is not Palindrome"<<endl;
        }
    }
    ~stack()
    {
        cout << "\nThankYOU!!" << endl;
    }
};

int main()
{
    stack s;
    cout<<"\nEntre a string: ";
    string data,Data;
    Data=" ";
    getline(cin,data);
    int len=data.length();          //65    90
    for(int i=0;i<=len;i++)         //97    122
    {
        if((int)data[i]<=90 && (int)data[i]>=65)
        {
            Data[i]=(char)((int)data[i]+32);
        }
        else if((int)data[i]<=122 && (int)data[i]>=97)
        {
            Data[i]=(char)((int)data[i]);
        }
    }
    for(int i=0;i<=len;i++)
    {
        s.push(Data[i]);
    }
    s.revstk();

    return 0;
}

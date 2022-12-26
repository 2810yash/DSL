#include <iostream>
#define MAX 10
using namespace std;

class CirQue
{
public:
    char que[MAX], a;
    int F, R;

// public:
    CirQue()
    {
        F = -1;
        R = -1;
    }
    bool isFull()
    {
        if ((R + 1) % MAX == F)
            return 1;
        else
            return 0;
    }
    bool isEmpty()
    {
        if (F == -1 && R == -1)
            return 1;
        else
            return 0;
    }
    void EnQue(char a);
    void DeQue();
    void Display();
};

void CirQue::EnQue(char a)
{
    if (isFull())
        cout << "Queue is full" << endl;
    else
    {
        if ((F == -1) && (R == -1))
            F++;
        // cout << "Enter Element: ";
        // cin >> a;
        R = (R + 1) % MAX;
        que[R] = a;
    }
};

void CirQue::DeQue()
{
    if (isEmpty())
        cout << "Queue is already Empty" << endl;
    else
    {
        char data;
        data = que[F];
        if (F == R)
            F = R = -1;
        else
            F = (F + 1) % MAX;
    }
    // return data;
};

void CirQue::Display()
{
    // cout<<"Delete element is: "<<a<<endl;
    cout << "\nRemaining queue is: ";
    int i = F;
    while (i <=R)
    {
        cout << que[i] << "\t";
        i++;
    }
};

int main()
{
    CirQue cq;
    char data;
    cq.EnQue('A');
    cq.EnQue('B');
    cq.EnQue('C');
    cq.EnQue('D');
    cq.Display();
    cq.DeQue();
    cq.Display();

    return 0;
}
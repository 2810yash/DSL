#include <iostream>
#define MAX 10
using namespace std;

class Queue
{
    int que[MAX];
    int F, R;

public:
    Queue()
    {
        F = -1;
        R = -1;
    }
    bool isFull();
    bool isEmpty();
    void EnQue();
    int DeQue();
    void display();
    ~Queue()
    {
        cout << "\nThankYou!!" << endl;
    }
};

bool Queue::isFull()
{
    if (R == MAX - 1)
        return 1;
    else
        return 0;
};

bool Queue::isEmpty()
{
    if (F == R)
        return 1;
    else
        return 0;
};

void Queue::EnQue()
{
    while (true)
    {
        if (isFull())
            cout << "Queue is full" << endl;
        else
        {
            R++;
            cout << "Entre element: ";
            cin >> que[R];
            cout << "Want to add more?(y/n): ";
            char ch;
            cin >> ch;
            if (ch == 'n')
                break;
        }
    }
};

int Queue::DeQue()
{
    int data;
    if (isEmpty())
        cout << "Queue is already Empty" << endl;
    else
    {
        data = que[F];
        F++;
        if (isEmpty())
            F=R=-1;
    }
    return data;
};

void Queue::display()
{
    int i = F;
    while (i < R)
    {
        i++;
        cout << que[i] << "\t";
    }
    cout << endl;
};

int main()
{
    Queue q1;
    int ch,x;
    do
    {
        cout << "\t\t1.Create Queue\n\t\t2.Delete an element\n\t\t3.Display\n\t\t4.Exit\nEnter your choose: ";
        cin >> ch;
        switch (ch)
        {
        case 1:
        {
            q1.EnQue();
            q1.display();
            break;
        }
        case 2:
        {
            x = q1.DeQue();
            cout << "Dequed element is " << x << endl;
            q1.display();
            break;
        }
        case 3:
            q1.display();
            break;
        default:
            break;
        }
    } while (ch != 4);

    return 0;
}
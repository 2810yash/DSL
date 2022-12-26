// Department of Computer Engineering has student's club named 'Pinnacle Club'.
// Students of second, third and final year of department can be granted membership on request.
// Similarly one may cancel the membership of club.
// First node is reserved for president of club and last node is reserved for secretary of club.
// Write C++ program to maintain club member‘s information using singly linked list.
// Store student PRN and Name. Write functions to:
// Add and delete the members as well as president or even secretary.
// Compute total number of members of club
// Display members
// Two linked lists exists for two divisions. Concatenate two lists.

#include <iostream>
#include <string.h>
using namespace std;

struct node
{
    string name;
    int PRN, Sr_no;
    node *next;
};

class Pinnacle
{
private:
    int count;
    node *president, *secretary, *temp, *temp1, *temp2;

public:
    Pinnacle();
    int create();
    void display(int);
    ~Pinnacle();
};

Pinnacle::Pinnacle()
{
    cout << "Welcome to club Pinnacle" << endl;
    president = NULL;
    count = 1;
};

int Pinnacle::create()
{
    char ch;
    do 
    {
        temp = new node;
        cout << "Enter your name: ";
        cin >> temp->name;
        cout << "Enter your PRN: ";
        cin >> temp->PRN;
        temp->Sr_no=count;
        temp->next=NULL;
        if (president==NULL)
        {
            president=temp;
            count++;
        }
        else
        {
            temp1=president;
            while (temp1->next!=NULL)
            {
                temp1=temp1->next;
            }
            temp1->next=temp;
            count++;
        }
        cout<<"Want to add more elements ?(y/n): ";
        cin>>ch;
    }while(ch!='n');
    return count;
};

void Pinnacle::display(int count)
{
    temp2=president;
    cout<<"SrNo\t\tPRN\t\tName\t\tPosition"<<endl;
    while (temp2!=NULL)
    {
        string position;
        if(temp2->Sr_no==1)
            position="President";
        else if(temp2->Sr_no==count-1)
            position="Secretary";
        else
            position="Member";
        cout<<temp2->Sr_no<<"\t\t"<<temp2->PRN<<"\t\t"<<temp2->name<<"\t\t"<<position<<endl;
        temp2=temp2->next;
    }
    cout<<endl;
};

Pinnacle::~Pinnacle()
{
    cout << "ThankYou!!" << endl;
};

int main()
{
    Pinnacle p1;
    int value;
    value=p1.create();
    p1.display(value);
    
    return 0;
}
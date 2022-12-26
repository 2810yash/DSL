# Write a python program to store names and mobile numbers of your friends in sorted order on names. 
    # Search your friend from list using binary search (recursive and non- recursive). 
    # Insert friend if not present in phonebook

def Binary_Search(N,list,num):
    left,right=0,N-1
    while(left<=right):
        mid=(right-left//2)
        if(num==list[mid][0]):
            return mid+1
        elif(num<list[mid][0]):
            right=mid-1
        elif(num>list[mid][0]):
            left=mid+1
    return -1

def Recursive(list,num,right,left,mid):
    if(num==list[left][0]):
        return left+1
    elif(num==list[right][0]):
        return right+1
    elif(num==list[mid][0]):
        return mid+1
    elif(num<list[mid][0]):
        right=mid-1
        mid=(right-left)//2
        return Recursive(list,num,right,left,mid)
    elif(num>list[mid][0]):
        left=mid+1
        mid=(right-left)//2
        return Recursive(list,num,right,left,mid)
    return -1

list=[]
N=int(input("Entre number of student you want: "))
for i in range(N):
    book=[]
    name=input(f"Name of person {i+1}: ")
    number=int(input(f"Number of person {i+1}: "))
    book.append(name)
    book.append(number)
    list.append(book)
list.sort()
print("List you enter is in sorted manner\n",list)
num=input("Enter person name you want to search: ")
while(1):
    ch=int(input("\n\t\t1.Non-Recursive\n\t\t2.Recursive\nEnter your choose: "))
    if(ch==1):
        position=Binary_Search(N,list,num)
        if(position!=(-1)):
            print(f"Number found at {position} position")
        else:
            print("Number you enter is not available in given list")
    elif(ch==2):
        left,right=0,N-1
        mid=(N//2)
        position=Recursive(list,num,right,left,mid)
        if(position!=(-1)):
            print(f"Number found at {position} position")
        else:
            print("Number you enter is not available in given list")

    d=input("Want to add more?(y/n)")
    if(d=='n'):
        break
# Write a python program to store roll numbers of student in array who attended training program in random order. 
# Write function for searching whether particular student attended training program or not, 
    # using Linear search and Sentinel search.

def linear_search(N,num,list,flag):
    for i in range(0,N):
        if(list[i]==num):
            print("Roll NO. found on ",i+1," position.")
            break
        else:
            flag+=1
    if (flag==N):
        print("Roll NO. not found")

#123 2
def sentinel_search(N,num,list): 
    list.append(num)
    i=0
    while(list[i]!=num):
        i+=1
    if(i<N):
        print("Roll NO. found on ",i+1," position.")
    else:
        print("Roll NO. not found")

list=[]
flag=0
N=int(input("Enter number of students those how have attended training program: "))
for i in range(0,N):
    rn=int(input("Enter your roll no.: "))
    list.append(rn)
num=int(input("Enter roll no. you want to search: "))
ch=int(input("\t\t1.Linear Search\n\t\t2.sentinel Search\nEnter your choose: "))
if(ch==1):
    linear_search(N,num,list,flag)
elif(ch==2):
    sentinel_search(N,num,list)

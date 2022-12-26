# Write a python program to store first year percentage of students in array. 
# Write function for sorting array of floating point numbers in ascending order using
    # Selection Sort
    # Bubble sort and display top five scores

def Selection_Sort(N,list):
    for i in range(0,N):
        mini=min(list[i::])
        a=0
        while(list[a]!=mini):
            a+=1
        list[i],list[a]=list[a],list[i]
    print("Sorted list is: ",list)

def Bubble_sort(N,list):
    for i in range(0,N):
        for j in range(0,N-i-1):
            if(list[j+1]<list[j]):
                list[j+1],list[j]=list[j],list[j+1]
    print("Sorted list is: ",list)

list=[]
N=int(input("Enter size of array(>5): "))
for i in range(0,N):
    marks=int(input("Entre your marks: "))
    list.append(marks)
ch=int(input("\t\t1.Selection Sort\n\t\t2.Bubble sort\nEnter your choose: "))
if(ch==1):
    Selection_Sort(N,list)
elif ch==2:
    Bubble_sort(N,list)
print("Top 5 scores are : ")
for i in range(6,1,-1):
    print(list[i],end=",")
# Write a Python program to compute following operations on String:
    # To display word with the longest length
    # To determines the frequency of occurrence of particular character in the string
    # To check whether given string is palindrome or not
    # To display index of first appearance of the substring
    # To count the occurrences of each word in a given string

str=input("Enter the string: \n")
print(str.split())
long=max(str.split(),key=len)
print("The longest word is: ",long)

a=input("Enter a characteryou want:  ")
count=0
for i in str:
    if i==a:
        count=count+1
print("character: ",a)
print("frequency: ",count)

rev = reversed(str)
if list(str) == list(rev):
    print('palindrome')
else :
    print('not a palindrome')

s=input("Enter the substring to find ")
print('The index of sub string is : ')
print(str.find(s))

mylist=str.split()
myset=mylist
mydict={}
for i in myset:
    mydict[i]=mylist.count(i)
print(mydict)
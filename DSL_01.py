# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class.
# Write functions to compute following:
# The average score of class
# Highest score and lowest score of class
# Count of students who were absent for the test
# Display mark with highest frequency

class Student:

    def __init__(self):
        self.marks=[]
        self.s,self.count,self.sum,self.avg=0,0,0,0

    def getdata(self,N):
        for i in range(0,N):
            self.s+=1
            print("Student",self.s,": ",end="")
            m=int(input())
            self.marks.append(m)
            if(m==-1):
                self.count+=1
            else:
                self.sum+=m
                self.avg=self.sum/(N-self.count)
        return (self.marks,self.avg,self.count)

    def frequency(self,N,score,high,low):
        max_freq = 0
        freqmarks = 0
        for i in range(0,N):
            if(score[i]!=(-1)):
                for j in range(0,N):
                    if(high<score[j]):
                        high=score[j]
                    elif(low>score[i]):
                        low=score[i]
            if(score.count(score[i]) > max_freq):
                max_freq = score.count(score[i])
                freqmarks = score[i]
        return(high,low,freqmarks)

score=[]
s=Student()
N=int(input("Enter total number of student: "))
score,avg,abs=s.getdata(N)
low=score[0]
high=low
high,low,frequency=s.frequency(N,score,high,low)
print("Average score of class is: ",avg)
print("Highest score of class is: ",high)
print("Lowest score of class is: ",low)
print("Number of student absent are: ",abs)
print("Frequency of highest score is: ",frequency)
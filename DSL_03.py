# Write a python program to compute following computation on matrix:
    # Addition of two matrices
    # Subtraction of two matrices
    # Multiplication of two matrices
    # Transpose of a matrix

row=int(input("Enter no. of rows: "))
column=int(input("Enter no. of columns: "))
A=[]
print("Enter elements for metrics A")
for i in range(row):
    r = []
    for j in range(column):
        n=int(input("Enter element: "))
        r.append(n)
    A.append(r)
B=[]
print("Enter elements for metrics B")
for i in range(row):
    r = []
    for j in range(column):
        n=int(input("Enter element: "))
        r.append(n)
    B.append(r)

def display(Metrics):
    for i in range(row):
        for j in range(column):
            print(Metrics[i][j],end=" ")
        print()

print()
display(A)
print()
display(B)
print()

def Transpose(metrics):
    for i in range(row):
        for j in range(column):
            print(metrics[j][i],end=" ")
        print()

def add(A,B):
    C=[]
    for i in range(row):
        c=[]
        for j in range(column):
            c.append(0)
        C.append(c)
    for i in range(row):
        for j in range(column):       
            C[i][j]=A[i][j]+B[i][j]
        
    display(C)

def subtraction(A,B):
    D=[]
    for i in range(row):
        d=[]
        for j in range(column):
            d.append(0)
        D.append(d)
    for i in range(row):
        for j in range(column):       
            D[i][j]=A[i][j]-B[i][j]
        
    display(D)

def multiplication(A,B):
    M=[]
    for i in range(row):
        m=[]
        for j in range(column):
            m.append(0)
        M.append(m)
    for i in range(row):
        for j in range(column):
            for k in range(row):    
                M[i][j]+=A[k][j]*B[i][k]
    display(M)

print("\nAddition is: ")
add(A,B)
print("\nSubtraction is: ")
subtraction(A,B)
print("\nMultiplication is: ")
multiplication(A,B)
print("\nTranspose of A is: ")
Transpose(A)
print("\nTranspose of B is: ")
Transpose(B)


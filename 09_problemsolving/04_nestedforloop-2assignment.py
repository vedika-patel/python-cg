#Q-1
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
#Q-2
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,"x",j,"=",i*j)
#Q-3
str=input("enter the string:")
for i in range(1,4):
    for j in range(1,5):
        print(str,end="")
    print()
#Q-4
row=int(input("enter the row:"))
column=int(input("enter the column:"))
for i in range(0,row):
    for j in range(0,column):
        print((i,j),end=" ")
    print()
#Q-5
n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
#Q-6
n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
#Q-7
n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#Q-8
n=int(input("enter the row:"))
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()
#Q-9
row=int(input("enter the row:"))
column=int(input("enter the column:"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print("*",end="")
    print()
##Q-10
N = int(input("Enter N: "))

for i in range(N):
    for j in range(N):
        print(j % 2, end="")
    print()  

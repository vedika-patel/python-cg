#Q-1:
for row in range(3):
    for colum in range(3):
        print("*",end=" ")
    print()    
#Q-2
for i in range(3):
    for j in range(1):
       print("1 2 3",end=" ")
    print()  
#Q-3
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()  
#Q-4
n=int(input("enter row:"));
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()  
#Q-5
n=int(input("enter the n:"))
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#Q-6    
n=int(input("enter row:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  
#Q-7
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()  
#Q-8
num=int(input("enter table number:"))
for i in range(1,11):
    for j in range(1):
        num=5*i
        print(num)
#Q-9
for i in range(1,6):
    for j in range(1,11):
        mul=i*j
        print(mul,end=" ")
    print()    
#Q-10
row=int(input("enter the row:"))
for i in range(1,row+1):
    for j in range(1,6):
        print(j**2,end=" ")
    print()  
 #Q-11
n=int(input("enter the row:"))
for i in range(n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print() 
 #Q-12
for i in range(6):
    for j in range(i+1):
        print(chr(65+i),end=" ") 
    print()      
#Q-13
for i in range(1,6):
    for j in range(1,i+1):
        print(2*j-1,end=" ")
    print()
#Q-14
for i in range(1,6):
    for j in range(1,i+1):
        print(2*j,end=" ")
    print()
#Q-15
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
#Q-16 
for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()    
#Q-17
for i in range(1,10,2):
    for j in range(1,i+1):
        if j%2 == 1:
            print(j,end=" ")
    print()
count=1     
for i in range(3):
    for j in range(3):
        print(count,end=" ")
        count += 1
    print() 
#Q-18
count=1
for i in range(1,5):
    for j in range(1,6):
        print(count,end=" ")
        count += 1
    print()  
#Q-19
for i in range(1,4):
    for j in range(1,4):
        print((i,j),end="")
    print()        
#Q-20
for i in range(1,4):
    for j in range(1,4):
        print(i,j)  
#Q-21
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print() 
#Q-23   
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
#Q-24   
for i in range(5):
    for j in range(5,i,-1):
        print(j,end=" ")
    print() 
#Q-25
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()    
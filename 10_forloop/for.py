# Q-1
for i in range(1,6):
    print("Hello")
# Q-2
for i in range(0,10):
    print(i,end=" ")
#Q-3
for i in range(1,11):
    print(i)
#Q-4
for i in range(10,0,-1):
    print(i)
#Q-5:
for i in range(5,51,5):
    print(i)
#Q-6:
for i in range(2,21,2):
    print(i)
#Q-7:
for i in range(1,20,2):
    print(i)
#Q-8:
for i in range(3,19,3):
    print(i)
#Q-9:
for i in range(20,0,-2):
    print(i)
#Q-10:
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(i)   
#Q-11:
n=int(input("enter the number:"))
for i in range(1,n+1):
    if i%2 == 0:
        print(i)
#Q-12:
n=int(input("enter the n:"))
for i in range(1,n+1):
    if i%2 == 1:
        print(i)
#Q-13:
n=int(input("enter the number n:"))
for i in range(1,n+1):
    if i%3 == 0:
        print(i)
#Q-14:
n=int(input("enter the number n:"))
for i in range(1,n+1):
    if i%2 == 0 and i%3 == 0:
        print(i)
#Q-15:
n=int(input("enter the number n:"))
count=0
for i in range(1,n+1):
    if i%2 == 0:
        count=count+1
print(f"total event number from the 1 to {n} is:{count}")
#Q-16:
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum) 
#Q-17:
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    if i%2 == 0:
        sum=sum+i
print(f"sum of the even numbers= {sum}") 
#Q-18:
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    if i%2 == 1:
        sum=sum+i
print(f"sum of the odd number is:{sum}")
#Q-19:
n=int(input("enter n:"))
for i in range(1,n+1):
    print(f"{n}x{i}={n*i}")
Q-20:
num=int(input("enter num:"))
fact=1
for i in range(1,num+1):
     fact=fact*i
     print(fact)
Q-21:
str=input("enter your string:")
for char in str:
    print(char)
Q-22:
str=input("enter your string:")
for char in str:
    print(char,end=" ")
Q-23:
str=input("enter your string:")
count=0
for char in str:
    count=count+1
    print("char",count)
Q-24:
str=input("enter your string:")
count=0
for char in str:
    if char == "a":
        count=count+1
print(count)
Q-25:
str=input("enter your string:")
count=0
for char in str:
    if  "A"<= char <="Z":
        count=count+1
print(f"uppercase chars counting:{count}")
Q-26:
for i in range(3):
    for j in range(4):
        print("*",end="")
    print() 
Q-27:
for row in range(4):
    for coulam in range(5):
        print("*",end="")
    print() 
Q-28:
for row in range(1,6):
    for coulam in range(1,row+1):
        print("*",end="")
    print()
Q-29:
for row in range(1,6):
    for colum in range(1,row+1):
        print(colum,end="")
    print() 
Q-30:
for i in range(1,6):
    i=i*5
    print(f"multipication result:{i}")
num=int(input("enter your number:"))
for i in range(num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    
                   

   
    
   





        

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
   





        

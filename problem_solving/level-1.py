## Level 1 – Basics (numbers, variables, if-else)
#Q-1 Even or Odd
num=int(input("enter the number:"))
if num%2 == 0:
    print("even")
else:
    print("odd")    
#Q-2
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
if a>b:
    print("output:",a)
else:
    print("outout:",b)   
#Q-3
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
if a>=b and a>=c:
    print("output:",a)
elif b>=c and b>=a:
    print("output:",b)
else:
    print("output:",c)    
#Q-4
num=int(input("enter the num:"))
if num>0:
    print("positive")
elif num<0:
    print("negative") 
else:
    print("zero") 
#Q-5
age=int(input("enter the age:"))
if age<=12:
    print("child")
elif age<=19:
    print("teenager")
else:
    print("adult") 
#Q-6
marks=float(input("enter the matks:"))
if marks>=90:
    print("A")
elif marks>=80:
    print("B") 
elif marks>=70:
    print("C") 
elif marks>=60:
    print("D")
else:
    print("F")    
#Q-7
num=int(input("enter the number:"))
if num%5 == 0:
    print("divisible by 5")
else:
    print("Not divisible by 5")  
#Q-8
num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5") 
#Q-9
year=int(input("enter the year:"))
if year%4==0:
    print("leap year") 
else:
    print("not a leap year")  
#Q-10
num=int(input("enter the number:")) 
if 10<=num<=50:
    print("in range")
else:
    print("not of range")    
                 

 
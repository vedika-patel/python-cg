number = int(input("Enter a number: "))
if number > 10:
    print("The number is greater than 10.")
age = int(input("Enter your age: "))
if age >= 18: 
    print("adult") 
positive_number = int(input("Enter a positive number: "))
if positive_number > 0:
    print("The number is positive.") 
mark=int(input("Enter your mark: "))
if mark >= 40:
    print("pass") 
else:  
    print("fail")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
positive_number = int(input("Enter a positive number: "))
if positive_number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

age = int(input("Enter your age: ")) 
if age >=18:
    print("adult")
else:
    print("minor")
even_number = int(input("Enter an even number: "))
if even_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is not even.")
odd_number = int(input("Enter an odd number: "))
if odd_number % 2 != 0:
    print("The number is odd.")
else:
    print("The number is not odd.")

marks = int(input("Enter your marks: "))
if marks >= 40:
    print("pass")
else:
    print("fail") 

a=19
b=20
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")  
# 11 to 20 question
mark=int(input("Enter your mark: "))
if mark >= 90:
    print("A grade")
elif mark >= 80:
    print("B grade")
elif mark >= 70:
    print("C grade")
elif mark >= 40:
    print("D grade")
else:
    print("F grade")

number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")   
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

number_of_days=int(input("Enter number of days: "))
if number_of_days == 1:
    print("Monday")    
elif number_of_days == 2:
    print("Tuesday")
elif number_of_days == 3:
    print("Wednesday")
elif number_of_days == 4:
    print("Thursday")
elif number_of_days == 5:
    print("Friday")
elif number_of_days == 6:
    print("Saturday")
elif number_of_days == 7:
    print("Sunday")
else:
    print("Invalid input")
students_marks=int(input("Enter your marks: "))
if students_marks >= 90:
    print("excellent") 
elif students_marks >= 80:
    print("good")
elif students_marks >= 40:
    print("pass")
else:
    print("fail")

if number==1:
    print("one")
elif number==2:
    print("two")
elif number==3:
    print("three")
else:
    print("other")

if age >= 18 and age <= 60:
    print("adult")

marks=int(input("Enter your marks: "))
if marks >= 90:
    print("excellent")
    if marks >= 80:
        print("good")
        if marks >= 40:
            print("pass")
        else:
            print("fail")
number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")

age=int(input("Enter your age: "))
if age >= 18:   
    print("adult")
    if age >= 60:
        print("senior citizen")
    else:
        print("not a senior citizen")
# 20. Nested - non-zero check

num = int(input("Enter a number: "))

if num != 0:
    if num > 0:
        print("Positive and non-zero")
    else:
        print("Negative and non-zero")
else:
    print("Zero") 
# 21. Multiple Conditions using AND

age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")

num = int(input("enter your number:"))
if num < 10 or num > 100:
    print("special")
else:
    print("not special")
# 23. Age and has_id

age = int(input("Enter age: "))
has_id = input("Do you have ID? (True/False): ").lower() == "true"
# or you can take as: has_id = True / False directly

if age >= 18 and has_id == True:
    print("Allowed")
else:
    print("Not Allowed")
# 24. Both > 10

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 10 and num2 > 10:
    print("Both are greater than 10")
else:
    print("Condition not satisfied")
            
                     
        
##Part A — Intermediate Problems
##Problem 1: Valid Marks
# marks=int(input("enter the marks:"))
if 0<=marks<=100:
    print("valid marks")
else:
    print("Invalid marks") 
# Problem 2: Positive Integer
num=int(input("enter the num:"))
if num>=0:
    print("accepted number")
else:
    print("not accepted")  
#Problem 3: Age Validation
age=int(input("enter the age:"))
if 0<age<=120:
    print("valid age")
else:
    print("invalid age")    
#Problem 4: Menu Choice
print("1. View profile")
print("2. Edit profile")
print("3. Settings")
print("4. Exit")
menu=int(input("enter the menu:"))
match menu:
    case 1:
        print("valid input")
    case 2:
        print("valid input")
    case 3:
        print("valid input")
    case 4:
        print("valid input")
    case _:
        print("invalid input")                
##problem 5: Password Length
password = ""

while len(password.strip()) < 8:
    password = input("Enter a password (at least 8 characters): ")
    
    if len(password.strip()) < 8:
        print("Password is too short. It must contain at least 8 characters.")

print("Success! Your password has been accepted.")
# #Problem 6: Temperature Range
tem=float(input("enter the temprechure:"))
if -20<=tem<=45:
    print("valid temprecture")
else:
    print("invalid temprecture")  
# # Problem 7: Withdrawal Validation 
balance = 5000.0
print(f"Current Balance: ₹{balance}")
while True:
    withdrawal = float(input("Enter withdrawal amount (₹): "))
    if withdrawal <= 0:
        print("Invalid amount. Withdrawal must be greater than zero.")
    elif withdrawal > balance:
        print("Insufficient funds. Withdrawal amount cannot exceed your balance.")
    else:
        break
balance -= withdrawal
print(f"Withdrawal successful! Remaining balance: ₹{balance}")
##Problem 8: Username Validation
while True:
    username = input("Enter a username: ")
    trimmed_username = username.strip()
    if len(trimmed_username) >= 5 and " " not in trimmed_username:
        print("Username accepted!")
        print("Accepted username:", username)
        break
    else:
        print("Invalid username. Please make sure it is at least 5 characters long (excluding outer spaces) and contains no spaces inside.")
##Problem 9: Divisible Number
num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("accepted number")
else:
    print("not accepted number")  
# # Problem 10: Limited PIN Attempts
secret_pin = "2468"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    
    if entered_pin == secret_pin:
        print("PIN accepted! Access granted.")
        break
    else:
      attempts -= 1
      if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.")
else:
            print("Access denied. All attempts failed.") 
##Problem 11: Number Within a Range
num=int(input("enter the number:"))
if 10<=num<=50 and num%2==0:
    print("even")
else:
    print("odd")  
##Problem 12: Deposit Validation
balance = 2000.0
print(f"Current Balance: ₹{balance:.2f}")
while True:
    deposit = float(input("Enter deposit amount: "))
    
    if deposit > 0:
        balance += deposit
        print(f"Deposit successful! New Balance: ₹{balance:.2f}")
        break
    else:
        print("Invalid amount. Please enter a positive value greater than zero.")
#art B — Challenging Problems
##Problem 13: Integer Between 1 and 100
num=int(input("enter the number:"))
if 0<=num<=100:
    print("valid number")
else:
    print("Invalid number") 
# roblem 14: Marks and Result
marks=int(input("enter marks:"))
if marks>75:
    print("Distinction")
elif 60<marks<=75:
    print("First Class")
elif 35<=marks<=60:
    print("pass")
else:
    print("fail")  
# #Problem 15: Username and Password Validation
while True:
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if len(username) < 5:
        print("Username must contain at least 5 characters.")
    elif " " in username:
        print("Username must not contain spaces.")
    elif len(password.strip()) == 0:
        print("Password must not be blank.")
    elif len(password) < 8:
        print("Password must contain at least 8 characters.")
    else:
        print("Username and password are valid!")
    break    
##Problem 16: Calculator Input Validation
num1 = float(input("Enter first number: "))

while True:
    operator = input("Enter operator (+, -, *, /): ")

    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operator! Try again.")

while True:
    num2 = float(input("Enter second number: "))

    if operator == "/" and num2 == 0:
        print("Division by zero is not allowed. Try again.")
    else:
        break

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)
# #Problem 17: Banking Menu
balance = 10000
while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated balance: ₹", balance)
        else:
            print("Deposit amount must be greater than zero.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Updated balance: ₹", balance)
    elif choice == "4":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
##Problem 18: Validate Month and Day
while True:
    month = int(input("Enter month (1-12): "))
    if month < 1 or month > 12:
        print("Invalid month! Try again.")
        continue
    day = int(input("Enter day (1-31): "))
    if day < 1 or day > 31:
        print("Invalid day! Try again.")
        continue
    break
print("Valid month and day!")
print("Month:", month)
print("Day:", day)
##Problem 19: Product Quantity and Price
while True:
    quantity = int(input("Enter product quantity: "))
    if quantity > 0:
        break
    else:
        print("Quantity must be a positive integer.")
while True:
    price = float(input("Enter unit price: ₹"))
    if price > 0:
        break
    else:
        print("Price must be greater than zero.")
total = quantity * price
print("Total cost: ₹", total)
## Problem 20: Safe Average Calculator
while True:
    count = int(input("How many numbers do you want to enter (1-20)? "))
    if 1 <= count <= 20:
        break
    else:
        print("Invalid count! Enter a number from 1 to 20.")
total = 0
for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    total = total + num
average = total / count
print("Average:", average)
##Problem 22: Input Validation Without
num = 0
while num < 1 or num > 10:
    num = int(input("Enter an integer from 1 to 10: "))
    if num < 1 or num > 10:
        print("Invalid input! Try again.")
print("Valid number:", num)
#problem 23: Three Valid Scores

score1 = int(input("Enter score 1 (0-100): "))
while score1 < 0 or score1 > 100:
    print("Invalid score! Try again.")
    score1 = int(input("Enter score 1 (0-100): "))
score2 = int(input("Enter score 2 (0-100): "))
while score2 < 0 or score2 > 100:
    print("Invalid score! Try again.")
    score2 = int(input("Enter score 2 (0-100): "))
score3 = int(input("Enter score 3 (0-100): "))
while score3 < 0 or score3 > 100:
    print("Invalid score! Try again.")
    score3 = int(input("Enter score 3 (0-100): "))
total = score1 + score2 + score3
average = total / 3
print("Total:", total)
print("Average:", average)
##Problem 24: ATM Withdrawal With Denomination Rules
balance = 10000
amount = 0
while amount <= 0 or amount > balance or amount % 100 != 0:
    amount = int(input("Enter withdrawal amount: ₹"))
    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance!")
    elif amount % 100 != 0:
        print("Amount must be a multiple of ₹100.")
balance = balance - amount
print("Withdrawn amount: ₹", amount)
print("Remaining balance: ₹", balance)









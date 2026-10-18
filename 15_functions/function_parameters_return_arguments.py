#Practice Problems
#**Beginner**
#Q-1
def welcome():
    print("welcome to python")
welcome()
welcome()
welcome()
#Q-2
def greet(name):
    print("Hello",name)
greet("vedika")    
#Q-3
def show_number(number):
    print("the number passed")
show_number(3)    
#Q-4
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
#Q-5
def square(number):
    return number**2
result=square(4)
print(result)
#Q-6
def is_even(number):
    return number%2==0
result=is_even(int(input("enter the number:")))
print(result)
#Q-7
def get_full_name(first_name, last_name):
    return first_name+" "+last_name
result=get_full_name("vedika","patel")
print(result)
#Q-8
def introduce(name, city="Pune"):
    return name+" "+city
result=introduce("vedika")
print(result)
#Q-9
def subtract(a, b):
    return a-b
result=subtract(10,50)
print(result)
#Q-10
def get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a
smaller, larger = get_min_max(15, 7)
print("Smaller:", smaller)
print("Larger:", larger)
#Intermediate
#Q-11
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    return total, difference, product, quotient
result = calculate(10, 2)
print("Result tuple:", result)
total, diff, prod, quot = calculate(10, 2)
print("Sum:", total)
print("Difference:", diff)
print("Product:", prod)
print("Quotient:", quot)
#Q-12
def count_digits(number):
    return number>=0
result=count_digits(0)
print(result)
#Q-13
def classify_number(number):
    if number>0:
        print("positive")
    elif number==0:
        print("zero")
    else:
        print("negative")
result=classify_number(0) 
#Q-14
def  calculate_total(price, quantity=1):
    return price*quantity
result=calculate_total(200)
print(result)
#Q-15
def create_email(username, domain="example.com"):
    return username,domain
result=create_email("vedika")
print(result)
#Q-16
def format_name(first, last, uppercase=False):
    full_name = f"{first} {last}"
    if uppercase:
        return full_name.upper()
    return full_name
print(format_name("John", "Doe"))
print(format_name("John", "Doe", True))
#Q-17
def percentage(marks, total=100):
    return (marks/total)*100
result=percentage(marks=85)
print(result)
#Q-18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute
print(convert_minutes(5,60))
print(convert_minutes(5))
#Q-19
def student_details(name, age, city):
    print(name)
    print(age)
    print(city)
student_details(name="vedika",age="17",city="hmt")   
#Q-20
def bill(item, quantity=1, price=100):
    print("Item",item,"quantity",quantity,"price",price)
bill("lipbom",price=1000) 
#Q-21
def analyze_number(number):
    if number < 0:
        absolute_val = -number
    else:
        absolute_val = number
    is_even = (number % 2 == 0)
    if number == 0:
        digit_count = 1
    else:
        digit_count = 0
        temp = absolute_val
        while temp > 0:
            digit_count += 1
            temp //= 10
    return absolute_val, is_even, digit_count
print(analyze_number(-1234))
print(analyze_number(0))     
print(analyze_number(48))
#Q-22




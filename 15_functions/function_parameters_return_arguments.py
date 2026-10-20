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
Q-22
def calculate_stats(a, b, c):
    smallest=min(a,b,c)
    largest=max(a,b,c)
    total_sum=a+b+c
    return smallest,largest,total_sum
smllest,largest,total=calculate_stats(95,5,25)
print("smllest",smllest)
print("lergest",largest)
print("sum",total)
#Q-23
def make_sentence(subject, verb, object):
    return f"{subject} {verb} {object}."
result = make_sentence(object="Python", verb="loves", subject="CodingGita")
print(result)
#Q-24
def apply_discount(price, discount=0):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price
price_with_discount = apply_discount(200, 15)
print("Discounted Price:", price_with_discount)
price_without_discount = apply_discount(200)
print("Regular Price:", price_without_discount)
#Q-25
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus
result=calculate_pay(4,500,bonus=100)
print(result)
#Q-26
def get_coordinates(x=0, y=0):
    return x,y
result=get_coordinates(45,90)
print(result)
#Q-27
def compare(a, b):
    if a > b:
        relation = "A is greater"
        diff = a - b
    elif b > a:
        relation = "B is greater"
        diff = b - a
    else:
        relation = "Equal"
        diff = 0
    return relation, diff
result_relation, result_diff = compare(15, 25)
print("Relation:", result_relation)
print("Absolute Difference:", result_diff)
#Q-28
def convert_temperature(value, scale="C"):
    if scale=="C":
        return (value*9/5)+32
    else:
        return (value-32)*5/9
print(convert_temperature(25))
print(convert_temperature(25,"C"))
print(convert_temperature(77,"F"))
#Q-29
def calculate_result(marks, passing_marks=35):
    if marks>35 and passing_marks:
        print("pass")
    else:
        print("fail")
calculate_result(60,35)    
#Q-30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    total_cost = (quantity * price) + delivery_fee
    return total_cost
print(order_summary("Notebook"))
print(order_summary("Notebook", delivery_fee=20)) 








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
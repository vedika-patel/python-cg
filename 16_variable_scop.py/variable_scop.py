#12. Practice Problems
##Q-1
# def local():
#     city="himmatnagar"
#     print(city);
# local()
##Q-2
# school="glorius"
# def outer():
#     def inner():
#         print(school);
#     inner()
# outer()
##Q-3
# age=18
# if age>=18:
#     name="young"
# print(name) 
##Q-4
# for i in range(1,3):
#     name="vedika"
# print(name)
##Q-5
##ans=Scope is about visibility ("Where can I access this name?"). It determines which parts of your code are allowed to "see" and use a variable name. For example, a local variable inside a function is only visible inside that specific function block.
# Lifetime is about duration ("How long does the variable or its underlying value stay in memory?"). It refers to the span of time during program execution that a variable binding or its object remains allocated and available.
##Q-6
##ans=200 and 100
##Q-7
# clicks = 0
# def click():
#     clicks=0
#     clicks += 1
#     print(clicks)
# click()    
##Q-8
##ans=because the name is print the name is define the after print
##Q-9
# def outer_function():
#     message = "Hello from the enclosing scope!"
#     def inner_function():
#         print(message)
#     inner_function()
# outer_function()
##Q-10
# def create_list():
#     my_list = [10, 20, 30]
#     return my_list
# numbers = create_list()
# print("Original list returned:", numbers)
# numbers.append(40)
# numbers[0] = 99
# print("Modified list from caller:", numbers)
##Q-11
# def outer():
#     message="hello class!"
#     def inner():
#         print(message)
#     inner()
# outer()
# outer() 
# outer()  
##Q-12
##ANS=3,2,1
##Q-13
# def create_multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply
# double = create_multiplier(2)
# print(double(5)) 
##Q-15


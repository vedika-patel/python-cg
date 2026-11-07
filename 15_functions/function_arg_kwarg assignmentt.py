#Practice Questions
#Q-1
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
result = multiply_all(2, 3, 4, 2)
print("The result of multiplication is:", result)
##Q-2
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_profile(name="John", age=30, city="New York", occupation="Engineer")        
#Q-3
def make_message(name, /, *, greeting="Hello"):
    return f"{greeting}, {name}!"
message1 = make_message("Alice", greeting="Hi")
print(message1)
#Q-4
def threeperameter(a,b,c):
  return a+b+c
values=[4,5,6]
result=threeperameter(*values)
print("The result of addition is:",result)
#Q-5
def unpacked():
    person={"name":"John","age":30,"city":"New York"}
    print("The person details are")
    print("Name:",person["name"])
    print("Age:",person["age"]) 
unpacked()    
#Q-6
def docstring_example():
    """This function demonstrates the use of a docstring."""
    print("This is an example of a function with a docstring.")
docstring_example() 
#Q-7
def values(a,b):
    return a*b
result = values(2,3)
print("The area of the rectangle is:", result)


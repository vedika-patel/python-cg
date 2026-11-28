#1. Add Two Numbers
result=lambda a,b:a+b
print(result(10,20))
# 2. Find the Square
square=lambda a:a*a
print(square(6))
#3.Find the Cube
qube=lambda a:a**3
print(qube(3))
#4. Check Even or Odd
result=lambda n:"even" if n%2==0 else "odd"
print(result(7))
#5.Find the Greater Number
result=lambda a,b:a if a>b else b
print(result(45,32))
#6. Convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
sample_celsius = 25
print(celsius_to_fahrenheit(sample_celsius))
#7. Calculate the Length of a String
result=lambda str:len(str)
print(result("python"))
#8. Convert a String to Uppercase
result=lambda str:str.upper()
print(result("hello world"))
#9. Find the Last Character
result=lambda str:str[-1]
print(result("coding"))
#10. Calculate the Final Price
final_price = lambda price, discount: price - (price * discount / 100)
original_price = 1000
discount_percent = 10
print(final_price(original_price, discount_percent))
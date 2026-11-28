# 1. Print a Message N Times
def positive(n):
    if n==0:
        return 
    message="Hello"
    print(message)
    return positive(n-1)
positive(3)
#2. Print Even Numbers from 2 to N
def even_num(n):
    if n==0:
        return
    even_num(n-1) 
    if n%2==0:
        print(n,end=" ")  
even_num(10)  
# 3. Find the Sum of Odd Numbers from 1 to N 
def sum_odd(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return sum_odd(n - 1)
    return n + sum_odd(n - 2)
print(sum_odd(7))
#4. Count How Many Times a Digit Appears
def count_digit(number, target):
    if number == 0:
        return 1 if target == 0 else 0
    last_digit = number % 10
    if last_digit == target:
        return 1 + count_digit(number // 10, target)
    return count_digit(number // 10, target)
print(count_digit(52525, 5))
#5. Find the Product of Digits
def product_digits(n):
    if n == 0:
        return 0
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)
print(product_digits(234))
#6. Find the First Digit of a Number



    
    
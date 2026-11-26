# #Q-1
# ANS=2,1,stop,1,2
# #Q-2
#ANS= if n == 0:
        # return 0
####Q-3
def count(n):
    if n == 0:
        return 

    return count(n - 1)
print(count(3))
###Q-4
def answer(n):
    if n == 0:
        return 0
    return n + answer(n - 1)
print(answer(3))
#Section B — Basic Recursive Problems (30 marks)
###Q-5
def count_down(n):
    if n==0:
        return "Done!"
    print(n)
    return count_down(n-1)
print(count_down(3))
#Q-6
def count_up(n):
    if n==0:
        return 
    count_up(n-1)
    print(n)
count_up(4)
#Q-7
def sum_to(n):
    if n==0:
        return 0
    return n +sum_to(n-1)
print(sum_to(5))
print(sum_to(0))
#Q-8
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print(factorial(4))
print(factorial(0))
#Q-9
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)
print(digit_sum(583)) 
print(digit_sum(7))    
print(digit_sum(0))    

#Q-10 
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(2, 5))
#Q-11
#Q-12
#Q-13
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
#Section D — Edge Cases and Debugging (10 marks)
#16. Fix the factorial (3 marks)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(0))
##Q-17
def stop_at_zero(n):
    if n == 0:
        return

    stop_at_zero(n)
print(stop_at_zero(0))
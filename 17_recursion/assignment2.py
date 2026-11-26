### 1. Sum of Digits at Even Positions
def sum_even_positions(n, position=1):
    if n == 0:
        return 0
    digit = n % 10
    if position % 2 == 0:
        return digit + sum_even_positions(n // 10, position + 1)
    else:
        return sum_even_positions(n // 10, position + 1)
print(sum_even_positions(583246))  # 12
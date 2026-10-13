# A1. Output Prediction --- Easy
#Q1. Stop Before Printing 5
#output:1,2,3,4,finished
#Q2. Stop at the First Vowel
#output:s k y l
#Q3. break in a while Loop
##2 4 6
##A2. Write a Program --- Medium
#Q4. Stop at a Target Number
num=int(input("enter the number:"))
for i in range(1,num+1):
    if i==7:
        break
    print(i,end=" ")
#Q5. Find the First Matching Character
text = input("Enter a string: ")
target = input("Enter target character: ")

for ch in text:
    print(ch,end=" ")
    if ch == target:
        break
#Q6. Stop at a Negative Number
numbers = list(map(int, input("Enter numbers: ").split()))
for num in numbers:
    if num < 0:
        break
    print(num, end=" ")
# A3. Think Carefully --- Challenging
## Q7. `break` Only Exits the Inner Loop
##output:1 1
# 1 2
#2 1
# 2 2
#3 1
#3 2
#Q8. Search a Word






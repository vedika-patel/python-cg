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
sentence = input().strip()
target = input().strip()
words = sentence.split()
found = False
for word in words:
    if word == target:
        print("Found")
        found = True
        break
if not found:
    print("Not found")
#Section B --- Practice Problems on continue
#B1. Output Prediction --- Easy
#Q9. Skip Number 4
#output:1,2,3,5,6
#Q10. Skip Vowels
#output:d c t n
#Q-11continue in a while Loop
#output:1 2 4
#B2. Write a Program --- Medium
#Q12. Print Numbers That Are Not Multiples of 3
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")
#Q13. Remove a Chosen Character from Display
text = input("Enter a string: ")
char = input("Enter a character: ")
for ch in text:
    if ch == char:
        continue
    print(ch, end="")
#Q14. Print Only Passing Marks
marks = input("Enter marks separated by spaces: ").split()
for mark in marks:
    mark = int(mark)
    if mark < 40:
        continue
    print(mark, end=" ")
# B3. Think Carefully --- Challenging
## Q15. `continue` Does Not Skip the Whole Loop
#output:A1 B1,A3 B3,A4 B3
## Q16. Fix the Infinite Loop
#output:1 2 3 
## Q17. Count Non-Vowel Characters
word = input("Enter a word: ")
count = 0
for ch in word:
    if ch in "aeiou":
        continue
    count += 1
print(count)
#Section C --- Practice Problems on `for-else`
# C1. Output Prediction --- Easy
## Q18. Normal Completion
#output:1 2 3 done
## Q19. Completion After `continue`
#output:1 3 4 completed
## Q20. Completion After `break`
#output:1 2 outside loop
## Q21. Empty Iterable







# #Q-1:
# text = input("Enter a string: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# spaces = 0
# special = 0

# for ch in text:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch.isspace():
#         spaces += 1
#     else:
#         special += 1

# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special characters:", special)

# counts = {
#     "Uppercase": uppercase,
#     "Lowercase": lowercase,
#     "Digits": digits,
#     "Spaces": spaces,
#     "Special characters": special
# }

# categories = [name for name, count in counts.items()]

# if len(categories) > 1:
#     print("Tie")
# else:
#     print("Highest:", categories[0])
#Q-2
# for marks in range(1,11):
#     marks=float(input("enter your marks:"))
#     if marks >=75:
#         print("excellent")
#     elif marks>=50:
#         print("good")
#     elif marks>=35:
#         print("pass")
#     elif marks<35:
#         print("fail")           
# #Q-3
sen=input("enter the sentence:")
vowel=2
consonant=1
Digit=3
special_characture=4
if vowel>consonant and vowel>Digit and vowel>special_characture:
    print("vowel",vowel)
elif consonant>vowel and consonant>Digit and consonant>special_characture:
    print("consonant",consonant)
elif Digit>vowel and Digit>consonant and Digit>special_characture:
    print("Digits",Digit)
elif special_characture>vowel and special_characture>consonant and special_characture>Digit:
    print("special characture",special_characture)
else:
    print("Tie")    
        
        
       


  







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
# #Q-2
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
#Q-3
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# highest_score = 0
# highest_word = ""

# for word in words:
#     score = 0

#     for ch in word:
#         if ch.lower() in "aeiou":
#             score += 2
#         elif ch.isdigit():
#             score += 3
#         elif ch.isalpha():
#             score += 1
#         else:
#             score += 4

#     print(word, "=", score)

#     if score > highest_score:
#         highest_score = score
#         highest_word = word

# print("Highest scoring word:", highest_word)
# print("Highest score:", highest_score)
#Q-4
for i in range(1, 6):
    password = input(f"Enter password for user {i}: ")

    
    length_ok = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            
            has_special = True


    score = 0
    if length_ok:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(
        f"Password {i} Strength: {strength} ({score}/5 conditions satisfied)\n"
    )

#Q.4
sentence = input("Enter a sentence: ")

words = sentence.split()

short_count = 0
medium_count = 0
long_count = 0

for word in words:
    length = len(word)

    if length <= 3:
        category = "Short"
        short_count += 1
    elif 4 <= length <= 6:
        category = "Medium"
        medium_count += 1
    else:
        category = "Long"
        long_count += 1

    print(f"Word: '{word}' | Length: {length} | Category: {category}")

print("\n--- Summary ---")
print(f"Short words (<= 3): {short_count}")
print(f"Medium words (4-6): {medium_count}")
print(f"Long words (> 6): {long_count}")

#Q.5
for i in range(1, 6):
    num_input = input(f"Enter number {i}: ")

    # Convert to string and remove negative sign if present
    num_str = str(num_input).lstrip("-")

    even_count = 0
    odd_count = 0

    # Examine every character/digit using a loop
    for char in num_str:
        if char.isdigit():
            digit = int(char)
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Compare digit counts and determine output
    print(f"\nNumber: {num_input}")
    print(f"Even digits: {even_count}, Odd digits: {odd_count}")

    if even_count > odd_count:
        print("Result: Even occurs more")
    elif odd_count > even_count:
        print("Result: Odd occurs more")
    else:
        print("Result: Equal")
    print("-" * 30)

#Q.6

text = input("Enter a string: ")

processed_chars = ""

print("\n--- Repeated Character Report ---")

for char in text:
    
    if char in processed_chars:
        continue

    occurrence_count = 0
    for c in text:
        if c == char:
            occurrence_count += 1

    processed_chars += char


    if occurrence_count > 1:
        if occurrence_count == 2:
            classification = "Duplicate"
        elif 3 <= occurrence_count <= 4:
            classification = "Repeated"
        else:  # More than 4
            classification = "Highly Repeated"

        print(
            f"Character: '{char}' | Occurrences: {occurrence_count} | Classification: {classification}"
        )


  







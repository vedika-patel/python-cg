# Task 1 - Create Strings

name = "Your Name"  # using double quotes
city = 'Ahmedabad'  # using single quotes
fav_language = "Python" # using double quotes
message = 'I love coding!' # using single quotes

print(name)
print(city)
print(fav_language)
print(message)
print(f"Name: {name}, City: {city}, Language: {fav_language}, Message: {message}")
# Task 2 - Empty String

empty_str = ""
print(empty_str)
print(f"Length of empty string is: {len(empty_str)}")
print(f"Is it empty? {empty_str == ''}")
# Task 3 - String Information

text = "Python Programming"

print(f"Complete string: {text}")
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Third character: {text[2]}")
print(f"Second-last character: {text[-2]}")
# Task 4 - Positive Indexing

text = "Programming"

print(f"First character: {text[0]}") # P
print(f"Second character: {text[1]}") # r
print(f"Fifth character: {text[4]}") # r
print(f"Last character: {text[10]}") # g
# Task 5 - Negative Indexing

text = "Programming"

print(f"Last character: {text[-1]}") # g
print(f"Second-last character: {text[-2]}") # n
print(f"Third-last character: {text[-3]}") # i
print(f"First character using negative: {text[-11]}") # P
full_name="vedika patel"
print(full_name[0])
print(full_name[2])
print(full_name[5])
print(full_name[11])
text="python programming"
print(text[0:6])
print(text[7:18])
print(text[0:18])
print(text[0:5])
print(text[13:18])
# Task 8 - Slicing with Step

text = "ABCDEFGHIJKL"

# 1. Print every second character
print(text[::2])      # Output: ACEGIK
# logic: start=0, end=last, step=2 -> 0,2,4,6,8,10

# 2. Print every third character
print(text[::3])      # Output: ADGJ
# logic: 0,3,6,9

# 3. Print characters from index 1 to index 8 with step 2
print(text[1:8:2])    # Output: BDFH
# logic: index 1 to 7 -> B,C,D,E,F,G,H -> step 2 -> B,D,F,H

# 4. Reverse the string
print(text[::-1])     # Output: LKJIHGFEDCBA
# Task 8 - Slicing with Step

text = "ABCDEFGHIJKL"

# 1. Print every second character
print(text[::2])      # Output: ACEGIK
# logic: start=0, end=last, step=2 -> 0,2,4,6,8,10

# 2. Print every third character
print(text[::3])      # Output: ADGJ
# logic: 0,3,6,9

# 3. Print characters from index 1 to index 8 with step 2
print(text[1:8:2])    # Output: BDFH
# logic: index 1 to 7 -> B,C,D,E,F,G,H -> step 2 -> B,D,F,H

# 4. Reverse the string
print(text[::-1])     # Output: LKJIHGFEDCBA
# Task 10 - Slicing Challenge
# Create any string at least 10 characters

text = "CodingGita"

# 1. The first 3 characters
print(text[:3])      # Cod

# 2. The last 3 characters
print(text[-3:])     # ita

# 3. Middle characters (example)
print(text[3:7])     # ingG

# 4. Reverse
print(text[::-1])    # atiGgnidoC

# 5. Every second character
print(text[::2])     # Cdnia
text="python programming"
print(len(text))
num="vedika"
print(len(num))
email="mitulkumar"
print(len(email))
text = "Python Programming"
print(len(text))
first_name="vedika"
last_name="patel"
print(first_name+" "+last_name)
Name="vedika"
age="17"
city="himmatnagar"
print(name+" "+age)
print(str(name+" "+age))
print(age*3)
print(name*5)
print(city*10)
print(Name.upper())
print(city.lower())
print(city.capitalize())
print(Name.title())
print(city.swapcase())
print(Name.casefold())
message="Python is a programming language"
print("Python" in message)
print("programming" in message)
print("Java"in message)
print("language" in message)
print(message.find("Python"))
print(message.find("programming"))
print(message.find("language"))
print(message.find("Java"))
text="banana"
print(text.count("a"))
print(text.count("n"))
print(text.count("b"))
# Task 24 - Starts and Ends

filename = "student_notes.pdf"

print(f"Filename: {filename}")
print(f"Starts with 'student': {filename.startswith('student')}")
print(f"Ends with '.pdf': {filename.endswith('.pdf')}")
print(f"Ends with '.txt': {filename.endswith('.txt')}")
text = "I am learning Java"
print(text.replace("Java", "python"))
text = "apple apple apple"
print(text.replace("apple", "mango"))
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
fruit="apple,banana,mango,orange"
print(fruit.strip())
print(fruit.lstrip())
print(fruit.rstrip())
words = ["Python", "is", "easy"]
print(" ".join(words))
# Task 38 - Name Processor

# 1. Take input
full_name = input("Enter your full name: ")
check_char = input("Enter a character to check: ")

# 1. Remove extra spaces from beginning and end
cleaned_name = full_name.strip()

# 2. Display original input
print(f"\n1. Original Input: '{full_name}'")

# 3. Display cleaned name
print(f"2. Cleaned Name: '{cleaned_name}'")

# 4. Uppercase
print(f"3. Uppercase: {cleaned_name.upper()}")

# 5. Lowercase
print(f"4. Lowercase: {cleaned_name.lower()}")

# 6. Title case
print(f"5. Title Case: {cleaned_name.title()}")

# 7. Length of the name
print(f"6. Length of name: {len(cleaned_name)}")

# 8. First character
if len(cleaned_name) > 0:
    print(f"7. First character: {cleaned_name[0]}")
    # 9. Last character
    print(f"8. Last character: {cleaned_name[-1]}")
else:
    print("Name is empty after cleaning!")

# 10. Check whether name contains a particular character
if check_char in cleaned_name:
    print(f"9. Yes, '{check_char}' is present in '{cleaned_name}'")
else:
    print(f"9. No, '{check_char}' is not present in '{cleaned_name}'")

# Case-insensitive check (better version)
if check_char.lower() in cleaned_name.lower():
    print(f" (Case-insensitive: '{check_char}' found)")
   


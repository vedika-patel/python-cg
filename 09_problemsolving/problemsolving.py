# # levle-1 
# # question:1
# a=int(input("enter the number:"))
# if a>0:
#     print("positive")
# elif a<0:
#     print("Negative") 
# elif a==0:
#     print("Zero")
# # question:2
# b=int(input("enter the number:"))
# if b==0:
#     print("zero")
# elif b>0:
#     if b%2 == 0:
#         print("positive even") 
#     else:
#         print("positive odd") 
# elif b<0:
#     if b%2 == 0:
#         print("negative even") 
#     else:
#         print("negative odd")
# # question:3
# c=int(input("enter the first number:")) 
# d=int(input("enter the second number:")) 
# if c>d:
#     print(c)
# elif c<d:
#     print(d)
# else:
#     print("Both are equal")
# # question:4
# e=int(input("enter the num1:")) 
# f=int(input("enter the num2:")) 
# g=int(input("enter the num3:"))
# if e<=f and e<=g:
#     print(e)  
# elif f<=g and f<=e:
#     print(f) 
# else:
#     print(g)
# #question:5
# h=int(input("enter the num1:")) 
# i=int(input("enter the num2:")) 
# j=int(input("enter the num3:"))
# if h>=i and h>=j:
#     print(h)  
# elif i>=h and i>=j:
#     print(i) 
# else:
#     print(j)
# # question:6
# k=int(input("enter the number:"))
# if k%5 == 0 and k%11 == 0:
#     print("Divisible by both 5 and 11")
# elif k%5 == 0:
#     print("Divisible only by 5")
# elif k%11 == 0:
#     print("Divisible only by 11")
# else:
#     print("Divisible by neither") 
# # question:7
# l=int(input("enter the number:"))
# if l%3 == 0 and l%7 == 0:
#     print("Divisible by both 3 and 7")
# elif l%3 == 0:
#     print("Divisible only by 3")
# elif l%7 == 0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by neither") 
# # question:8
# marks=float(input("enter the  your marks:"))
# if marks<0 or marks>100:
#     print("invalide")
# elif marks>=40:
#     print("pass")
# else:
#     print("fail")
# # qustion:9
# marks=float(input("enter the  your marks:"))
# if marks<0 or marks>100:
#     print("invalid")
# elif marks>=90:
#     print("grade a")
# elif marks>=80:
#     print("grade b")
# elif marks>=70:
#     print("grade c")
# elif marks>=60:
#     print("grade d")
# elif marks>=40:
#     print("grade e")
# else:
#     print("fail")
# #question:10
# age=int(input("enter your age:"))
# if age<0 or age>120:
#     print("invalid")
# elif age>=18:
#     print("can vote")
# else:
#     print("cannot vote")
# # qustion:11
# year=int(input("enter year:"))
# if (year%400 == 0)or (year%4 ==0 and year%100 !=0):
#     print("leap year")
# else:
#     print("not a leap year")
# # qustion:12
# char=input("enter the charcter:")
# if 'A' <= char <= 'Z': 
#     print("Uppercase alphabet")
# elif 'a'<= char <='z':
#     print("Lowercase alphabet")
# elif '0'<= char <='9':
#     print("Digit")
# else:
#     print("Special character")
# # question:13
# #Take a single character input from the user
# char = input("enter the char:")

# # Check if the input is exactly one alphabetic character
# if len(char) == 1 and char.isalpha():
#     # Convert to lowercase to handle both upper and lower case
#     char_lower = char.lower()
    
#     # Check if the character is a vowel
#     if char_lower in ['a', 'e', 'i', 'o', 'u']:
#         print("Output: Vowel")
#     else:
#         print("Output: Consonant")
# else:
#     print("valid input")
# #question:14
# cost_price=float(input("enter the costprice:"))
# selling_price=float(input("enter the sellingprice:"))
# if selling_price>cost_price:
#     profit=selling_price-cost_price
#     print(f"profi= {profit}")
# elif selling_price<=cost_price:
#     loss=cost_price-selling_price
#     print(f"loss= {loss}")
# else:
#     print("No profit and no loss")
# #Question:15 
# cost_price=float(input("enter the costprice:"))
# selling_price=float(input("enter the sellingprice:"))
# if selling_price>cost_price:
#     Profit = selling_price -cost_price
#     profit_pasenger=Profit/cost_price*100
#     print(f"profit ={profit_pasenger} %")
# elif selling_price<cost_price:
#     loss=cost_price-selling_price
#     loss_pasnger=loss/cost_price*100
#     print(f"loss ={loss_pasnger} %")
# else:
#     print("envalid")
# question:16
# units=float(input("enter units:"))
# if units<=100:
#     print(f"total:{units*5}")
# elif units<=200:
#     first_hundrade=100*5
#     remaning=(units-100)*7
#     print(f"total:{first_hundrade+remaning}") 
# else:
#     first_hundrade=100*5
#     nexthundred=100*7
#     remaning=(units-200)*10
#     print(f"total:{first_hundrade+remaning+nexthundred}")
# question:17
# first_number=float(input("enter the first number:"))
# second_number=float(input("enter the second number:"))
# oprater=input("enter the oprater:")
# if oprater == "+":
#     print(first_number+second_number)
# elif oprater == "-":
#     print(first_number-second_number) 
# elif oprater == "*":
#     print(first_number*second_number) 
# elif oprater == "/":
#     if second_number != 0:
#         print(first_number/second_number)
#     else:
#         print("oprator is dont alow division by zero") 
# else:
#     print("invalid oprators")
# #Question:18
# temperature=float(input("enter the temperature:"))
# if temperature<=0:
#     print("Freezing")
# elif temperature<=15:
#     print("very cold")
# elif temperature<=25:
#     print("cold") 
# elif temperature<=35:
#     print("Normal")
# else:
#     print("Hot")               
# # Question:19
# number=float(input("enter the number:"))
# if number<=0:
#     print("Negative") 
# elif number<=10:
#     print(f"number is between 0 and 10")
# elif number<=50:
#     print(f"number is between 11 and 50") 
# elif number<=100:
#     print(f"number is between 51 and 100")
# else:
#     print("not valid number")   
# # Question:20
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if a + b > c :
#     if a + c > b:
#         if b + c >a:
#             print("Valid triangle") 
# else:
#      print("Invalid triangle")
# Question:21
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if a + b > c :
#     if a + c > b:
#         if b + c >a:
#             print("Valid triangle")
#             if a == b == c:
#                 print("Equilateral")
#             elif a == b != c:
#                 print("Isosceles")
#             elif a != b != c:
#                 print("Scalene")        
# else:
#      print("Invalid triangle")
# question:22
# A=float(input("enter your Account_balance:"))
# B=float(input("enter your Withdrawal_amount:"))
# if B>=0:
#     if B/100:
#         if B<A:
#             c=A-B
#             print(f"Withdrawal successful")
#             print(f"remaning balance:{c}") 
#Question:23
# User_name=input("enter your Username:")
# password=input("enter your password:")
# if User_name!= "admin":
#     print("User not found")
# elif password!= "python123":
#     print("Wrong password")
# else:
#     print("Login successful") 
#question:24
# purchase_amount=float(input("enter you purchase price:"))
# if purchase_amount<=500:
#      discountamount=(purchase_amount*0)/100
#      finalamount=purchase_amount-discountamount
#      print(f"discount:0%  discount amount:{discountamount}rs. final amount:{finalamount}rs.")
# elif purchase_amount<=999:
#      discountamount=(purchase_amount*5)/100
#      finalamount=purchase_amount-discountamount
#      print(f"discount:5%  discount amount:{discountamount}rs. final amount:{finalamount}rs.")
# elif purchase_amount<=1999:
#      discountamount=(purchase_amount*10)/100
#      finalamount=purchase_amount-discountamount
#      print(f"discount:10%  discount amount:{discountamount}rs. final amount:{finalamount}rs.")          
# elif purchase_amount<=4999:
#      discountamount=(purchase_amount*15)/100
#      finalamount=purchase_amount-discountamount
#      print(f"discount:15%  discount amount:{discountamount}rs. final amount:{finalamount}rs.")             
# else:
#       discountamount=(purchase_amount*20)/100
#       finalamount=purchase_amount-discountamount
#       print(f"discount:20%  discount amount:{discountamount}rs. final amount:{finalamount}rs.")             
# question:25
# mark1 = int(input("Enter marks for subject 1: "))
# mark2 = int(input("Enter marks for subject 2: "))
# mark3 = int(input("Enter marks for subject 3: "))

# if (mark1 < 0 or mark1 > 100 or
#     mark2 < 0 or mark2 > 100 or
#     mark3 < 0 or mark3 > 100):
#     print("Invalid marks")

# elif mark1 < 35 or mark2 < 35 or mark3 < 35:
#     print("Fail")

# else:
#     average = (mark1 + mark2 + mark3) / 3
#     print("Average:", average)

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")           
#question:26
day=int(input("enter your Day:"))
month=int(input("enter you month:"))
year=int(input("enter you year:"))




      
        






  




      








          


       
     
    

           
                
      
        

    
  
                 

                                                   
    
            
           
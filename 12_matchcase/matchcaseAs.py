#Q-1
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        print(" you selectedPizza")
    case 2:
        print("you selected Burger")
    case 3:
        print("you selected Pasta")
    case 4:
        print("you selected Sandwich")   
    case _:
        print("Invalid choice")
#Q-2
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        print("you selected wi-fi")
    case 2:
        print("you selected Bluetooth")
    case 3:
        print("you selected Mobile Data")
    case 4:
        print("you selected Arirplane Mode")   
    case _:
        print("Exit")
#Q-3
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        print("you selected Check Balance")
    case 2:
        print("you selected Withdraw Money")
    case 3:
        print("you selected Deposit Money")
    case 4:
        print("you selected Change PIN")   
    case _:
        print("Exit")
#Q-4
color=input("Enter your color: ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _ :
        print("Invalid signal")
#Q-5
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        print("Opening profile")
    case 2: 
        print("Opening Courses")  
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance") 
    case _:
        print("logout") 
#Q-6
category=int(input("Enter category: "))
match category:
    case 1:
        print("Electronics")
    case 2:
        print("opening Clothing")
    case 3:
        print("opening Grocery")  
    case 4: 
        print("opening books")
    case _:
        print("Exit")    
# Q-7
service=int(input("Enter your service: "))  
match service:
    case 1:
        print("opening Account Balance")
    case 2:
        print("opening mini statement")
    case 3:
        print("opening Fund Transfer")
    case 4:
        print("opening Bill Payment")
    case _:
        print("opening Customer Support") 
#Q-8
show=int(input("Enter your show: "))
match show:
    case 1:
        print("Morning Show selected")
    case 2:
        print("Afternoon Show selected")
    case 3:
        print("Evening Show selected")
    case 4:
        print("Night Show selected")
    case _:
        print("Invalid show")
# #Q-9

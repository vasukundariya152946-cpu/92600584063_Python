# 1. Write a program to demonstrate conditional  statements using if if-else and if-elif-else. 

# if Statment
age = int(input("Enter your age: "))
if age>18:
    print("You are eligible to vote.")
    
# if else statment
num = int(input("Enter any nuber = "))
if num %2==0:
    print("Number is Even ")
else:
    print("Number is  odd ")
# if-elif-else.
marks =int(input("Enter any markas ="))
if marks>90:
    print("Grade A ")
elif marks>75:
    print("Grade B")
elif marks>50:
    print("Grade C")
elif marks>33:
    print("Grade D")
else:
    print("Fail")
    
'''  output :
        Enter your age: 22
You are eligible to vote.
Enter any nuber = 4
Number is Even 
Enter any markas =65
Grade C'''
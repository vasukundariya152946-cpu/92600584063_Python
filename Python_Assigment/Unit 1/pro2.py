# 2. Write a program to illustrate the use of different data types and type casting.
name = "vasu"
age = 21
hight = 5.6
is_student = True
print("name :,",name, "Type :", type(name))
print("age :,",age, "Type :", type(age))
print("hight :,",hight, "Type :", type(hight))
print("is__student :,",is_student, "Type :", type(is_student))

num1="25"
num2=int(num1)
num3=float(num2)
num4=str(num2)
print("string to integer :-",num2)
print("integer to float :-",num3)
print("integer to string :-",num4)
'''
output:-
name :, vasu Type : <class 'str'>
age :, 21 Type : <class 'int'>
hight :, 5.6 Type : <class 'float'>
is__student :, True Type : <class 'bool'>

string to integer :- 25
integer to float :- 25.0
integer to string :- 25'''
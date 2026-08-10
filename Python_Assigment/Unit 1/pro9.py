# Write a program to define and use user-defined functions with different types of arguments.
def add(a,b):
    print("Addition :",a+b)
add(10,20)

def student(name,age):
    print("name :",name)
    print("age :",age)
student(name ="vasu",age=21)

def greet(name="vasu"):
    print("hello",name)
    
greet()

def total(*number):
    print("total :",sum(number))
total(10,20,30,40)

# output
# Addition : 30
# name : vasu
# age : 21
# hello vasu
# total : 100
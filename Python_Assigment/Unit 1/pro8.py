# # 8. Write a program to explain mutable and immutable objects in Python.
# Immutable object
a =(10,20,30,40,50,)
print(a)

name = "Vasu"
print(name)

name = name+" Patel"
print("After changing string",name)

# Mutable object

num =[10,20,30,40,50]
print(num)
num[0]=100
print("After changing list",num)
num.append(40)
print("After append list",num)

# output
# (10, 20, 30, 40, 50)
# Vasu
# After changing string Vasu Patel
# [10, 20, 30, 40, 50]
# After changing list [100, 20, 30, 40, 50]
# After append list [100, 20, 30, 40, 50, 40]
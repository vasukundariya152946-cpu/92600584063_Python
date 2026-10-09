# 2) Write a program to demonstrate different import mechanisms in Python.
import math
print ("Using Import Module :")
print("Square root of 25 = ",math.sqrt(25))
print("---------------------------------------")
from  math import factorial
print("Using From math import Factorical") 
print("Factorial of 5 =",factorial(5))
print("---------------------------------------")
from math import ceil,pow
print("Using  form module  import multiple fuction: ")
print(" 2 raised to 3 =",pow(2,3))
print("celling of 4.3= ",ceil(4.3))
print("---------------------------------------")
import math as m 
print(" Useing imoport module as alice ")
print(" value of PI =" ,m.pi)
print("---------------------------------------")
from math import sqrt as s 
print("Using from module import fuction as anlice ")
print("Square  root of 49 = ",s(49))

# otuput:-
# Using Import Module :
# Square root of 25 =  5.0
# ---------------------------------------
# Using From math import Factorical
# Factorial of 5 = 120
# ---------------------------------------
# Using  form module  import multiple fuction:
#  2 raised to 3 = 8.0
# celling of 4.3=  5
# ---------------------------------------
#  Useing imoport module as alice
#  value of PI = 3.141592653589793
# ---------------------------------------
# Using from module import fuction as anlice
# Square  root of 49 =  7.0
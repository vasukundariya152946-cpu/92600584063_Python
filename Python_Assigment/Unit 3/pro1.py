#1). Write a program to create and import a user- defined module.
import mymodule
a = int(input("Enter first Number :"))
b = int(input("Enter Second Number :"))
print("Addition :- ",mymodule.add(a,b))
print("Substraction :- ", mymodule.substract(a,b))
print("multipication :-", mymodule.multiply(a,b))
if b !=0:    
    print("Division:-",mymodule.divide(a,b))
else:
    print("Division is not  possible because denominator is zero")

# output:-
# Enter first Number :5
# Enter Second Number :3
# Addition :-  8
# Substraction :-  2
# multipication :- 15
# Division:- 1.6666666666666667
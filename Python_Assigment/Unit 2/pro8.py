#  Write a program to illustrate variable scope  using local global and nonlocal variables.
x=10 
def outer():
    y=20
    def inner():
        nonlocal y 
        y=30
        
        print("Global variable :",x)
        print("Nonlocal variable :",y)
    inner()
    print("local variable : ",y)
outer()

'''output:
    Global variable : 10
Nonlocal variable : 30
local variable :  30'''
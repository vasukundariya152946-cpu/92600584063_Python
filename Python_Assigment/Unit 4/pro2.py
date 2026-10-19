# Write a program to demonstrate constructor
# and destructor usage.
class student:
    def __init__(self,name):
        self.name=name 
        print("Coustructor called")
        print("Student Name:",self.name)
    def __del__(self):
        print("Destructor")
s1=student("Vasu")
del s1
# output :-
# Coustructor called
# Student Name: Vasu
# Destructor
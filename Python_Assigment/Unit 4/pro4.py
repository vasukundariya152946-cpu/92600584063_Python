# Write a program to demonstrate instance
# methods class methods and static methods.
class student:
    collage="marwadi university"
    def __init__(self,name):
        self.name=name 
    def display(self):
        print("student Name :",self.name)
    @classmethod
    def show_collage(cls):
        print("College Name:",cls.collage)
    @staticmethod
    def message():
        print("Welcome to Python Programming")
        
s1=student("Vasu")
s1.display()
student.show_collage()
student.message()
# output:-
# student Name : Vasu
# College Name: marwadi university
# Welcome to Python Programming
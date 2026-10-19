# # 
# Write a program to illustrate instance variables
# # and class variables
class student:
    collage="marwadi univarsity"
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Collge:",self.collage)
s1=student("vasu",22)
s2=student("riya",21)
s1.display()
print()
s2.display()
# output :
#     Name: vasu
# Age: 22
# Collge: marwadi univarsity

# Name: riya
# Age: 21
# Collge: marwadi univarsity
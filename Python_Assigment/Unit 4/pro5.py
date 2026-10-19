# Write a program to implement single multilevel
# and multiple inheritance.
class parent:
    def show_parant(self):
        print("this is Parant class")
class child(parent):
    def show_child(self):
        print("This is child class")
print("Single Inheritance")
c=child()

c.show_parant()
c.show_child()
# output:
#     Single Inheritance
# this is Parant class
# This is child class
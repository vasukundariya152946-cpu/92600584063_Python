# Write a program to illustrate method resolution
# order and magic methods.
class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("class B")
class C(A):
    def show(self):
        print("class C")
class D(B,C):
    pass

obj=D()
obj.show()
print("Mro:")
print(D.mro())

class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
s= student("vasu")
print(s)
# output :-
# class B
# Mro:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# vasu
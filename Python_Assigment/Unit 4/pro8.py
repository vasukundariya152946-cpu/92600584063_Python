# # Write a program to demonstrate encapsulation
# # and abstraction using classes.
from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
   
    def intrest(self):
        pass
class SBI(bank):
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def show_balance(self):
        print("Balance :",self._balance)
    def intrest(self):
        print("Intrest rate : 7%")
s1=SBI(5000)

s1.show_balance()
s1.deposit(2000)
s1.show_balance()
s1.intrest()
# output :-
# Balance : 5000
# Balance : 7000
# Intrest rate : 7%
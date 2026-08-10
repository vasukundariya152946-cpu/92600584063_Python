#  Write a program to find the sum of digits of  a number using a while loop.
num= int(input("Enter any number :"))
sum =0 
while num>0:
    digit =num % 10
    sum= sum+ digit
    num= num//10
print("Sum is a =",sum)

'''output :-
Enter any number :1234567
Sum is a = 28
'''
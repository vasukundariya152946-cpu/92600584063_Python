# . Write a program to demonstrate list dictionary and set comprehensions.
num = [1,2,3,4,5]
print(num)
sq =[x*x for x in num]
print("Square =",sq)

sq_digit ={x:x*x for x in num}
print("Square Digit :",sq_digit)

even_num={x for x in num if x % 2==0}
print("Even number : ",even_num)


'''output :
    [1, 2, 3, 4, 5]
Square = [1, 4, 9, 16, 25]
Square Digit : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Even number :  {2, 4}'''
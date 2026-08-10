# 5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.
num = [1,2,3,4,5,6,7,8,9,10]
print(num)
print("First element :",num[0])
print("Secend element :",num[1])
print("last element :",num[-1])
print("-----Slicing----------")
print("First Three element :",num[:3])
print("Last three element :",num[6:])
print("three to seven element:",num[2:6])

num.append(11)
print("After append: ", num)

num.remove(10)
print("After remove :", num)

squares = [x * x  for x in num]
print("Squares :",squares)

even_number = [x for x in num if x %2==0]
print("Even Number : ",even_number) 


''''output :-
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First element : 1
Secend element : 2
last element : 10
-----Slicing----------
First Three element : [1, 2, 3]
Last three element : [7, 8, 9, 10]
three to seven element: [3, 4, 5, 6]
After append:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
After remove : [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
Squares : [1, 4, 9, 16, 25, 36, 49, 64, 81, 121]
Even Number :  [2, 4, 6, 8]'''
# Write a program to demonstrate iterators and iterables in Python.
num = [10,20,30,40,50,60]
print(num)
print("Iterable:")
for i in num:
    print (i)
print(" Iterators:")
num_iter = iter(num)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

'''output :
    [10, 20, 30, 40, 50, 60]
Iterable:
10
20
30
40
50
60
 Iterators:
10
20
30
40
50
60'''
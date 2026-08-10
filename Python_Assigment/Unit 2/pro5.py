# Write a program to demonstrate the use of break continue and pass statements.
print("---------Break----------")
for i in range(1,11):
    if i ==4:
        break
    print(i)
print("---------Continue----------") 
for i in range(1,11):
    if i ==4:
        continue
    print(i)
print("---------Pass----------") 
for i in range(1,11):
    if i ==4:
        pass
    print(i)
    
    
''' output:
        ---------Break----------
1
2
3
---------Continue----------
1
2
3
5
6
7
8
9
10
---------Pass----------
1
2
3
4
5
6
7
8
9
10'''
def num_gen(n):
    for i in range(1,1+n):
        yield i
n=int(input("Enter Any number ="))

print("Number Of Sequence ")
for num in num_gen(n):
    print(num)
    
    '''output :
Enter Any number =6
Number Of Sequence 
1
2
3
4
5
6'''
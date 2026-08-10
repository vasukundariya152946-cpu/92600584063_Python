#  Write a program to check whether a number is  negative or zero using nested conditions
num = int(input("Enter any Number :"))
if num<=0:
    if num==0:
        print("Number is zero")
    else:
        print("Number is Nagativ")
else :
    print("Number is Possitive")
    
'''      
    output :
Enter any Number :4
Number is Possitive  
Enter any Number :0
Number is zero
Enter any Number :-2
Number is Nagativ'''
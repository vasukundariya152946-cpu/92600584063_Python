# 10.Write a program to demonstrate recursion using factorial or Fibonacci series.
def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        return n * factorial (n-1)
num =5
result = factorial(num)
print("factorial of",num,"is :",result)
 
'''  output :
      factorial of 5 is : 120'''
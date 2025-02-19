"""Recursions:-
Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function"""

"""Factorial(1) = 1
Factorial(2) =  2 x 1
Factorial(3) = 3 x 2 x 1
Factorial(4) =  4 x 3 x 2 x 1
Factorial(n) = n x n-1 x...3 x 2 x 1

Factorial(n)= n * factorial(n-1)

"""
# def factorial(n=1):
#    if(n==1 or n==0):
#       return 1
#    return n * factorial(n-1)
# a=factorial(6)
# print(a)
# factorial()

def factorial(n):
   if(n==1 or n==0):
      return 1
   else:
      return n * factorial(n-1)
n = int(input("Enter the number:"))
print(f"The factorial of {n} is {factorial(n)}")



"""
Python program to print factorial of a number. This code uses the recursion approach in which we will 
use a recursive function i.e. a function will call itself repeatedly to get the result.
"""

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num-1))


number = int(input("Enter a number to find it's factorial: "))
fact = factorial(number)
print(f"Factorial of the number {number} is {fact}")
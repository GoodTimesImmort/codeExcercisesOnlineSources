"""
File Name: fibFinder.py
Author: w3school.com
Reproduced: goodTimesImmort
Description: Fibonacci position finder.
[gT_I]: This function calls for input then uses recursion to calculate backwards. 
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#[gT_I] I modified the example to ask for input.
number = int(input("Enter a digit and I print what number is at that position in the Fibonacci sequence! "))

print(fibonacci(number))
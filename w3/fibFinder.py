def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#I modified the example to ask for input.
number = int(input("You want to know what number is in the Fibonacci sequence in what position? "))

print(fibonacci(number))
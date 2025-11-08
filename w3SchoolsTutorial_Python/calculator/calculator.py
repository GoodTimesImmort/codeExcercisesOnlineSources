"""
File Name: calculator.py
Author: w3school.com
Reproduced: goodTimesImmort
Description: This script is a simple text driven calculator.
[gT_I]: The script defines the math and memory with functions 
and then creates a loop for input and output. 
"""

# Basic Arithmetic Functions
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a/ b if b != 0 else "Error: Division by zero"

def exponentiate(a, b):
    return a ** b


# Memory Storage
memory = None

def store_memory(value):
    global memory
    memory = value
    print("Stored in memory.")

def recall_memory():
    return memory if memory is not None else "No value in memory."

def clear_memory():
    global memory
    memory = None
    print("Memory cleared.")


# Main Calculator Loop
def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Recall Memory (M)")
        print("7. Clear Memory (MC)")
        print("8. Exit (X)")

        choice = input("Enter choice: ").strip().lower()

        if choice in ['x', '8']:
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ['m', '6']:
            print("Memory: ", recall_memory())
            continue
        elif choice in ['mc', '7']:
            clear_memory()
            continue

        if choice not in ['1', '2', '3', '4', '5', '+', '-', '*', '/', '^']:
            print("Invalid input. Try again")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        if choice in ['1', '+']:
            result = add(num1, num2)
        elif choice in ['2', '-']:
            result = subtract(num1, num2)
        elif choice in ['3', '*']:
            result = multiply(num1, num2)
        elif choice in ['4', '/']:
            result = divide(num1, num2)
        elif choice in ['5', '^']:
                result = exponentiate(num1, num2)

        print("Result: ", result)

        store_option = input("Store result in memory? (y/n): ").strip().lower

        if store_option == 'y':
            store_memory(result)

# Ensures the script runs correctly when executed directly 
if __name__ == '__main__':
    calculator()
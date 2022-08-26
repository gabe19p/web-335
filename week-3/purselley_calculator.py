    # 
    # Title: purselley_calculator.py
    # Author: Danial Purselley
    # Date: 26 August 2022
    # Description: calculator application with python
    #

# addition function for two parameters
from audioop import mul


def add(a, b):
    return (a + b)
    

# subtraction function for two parameters
def subtract(a, b):
    return a - b

# division function for two parameters
def divide(a, b):
    return a / b

# multiplication function for two parameters
def multiply(a, b):
    return a * b

# number variables to go into the functions
num2 = 2
num4 = 4
num6 = 6
num8 = 8
num10 = 10

# test variables for each function
addition = f"{num4} + {num4} = {add(num4, num4)}"
subtraction = f"{num10} - {num6} = {subtract(num10, num6)}"
division = f"{num8} / {num2} = {divide(num8, num2)}"
multiplication = f"{num10} * {num2} = {multiply(num10, num2)}"

# printing each variable to display the function
print(addition)
print(subtraction)
print(division)
print(multiplication)
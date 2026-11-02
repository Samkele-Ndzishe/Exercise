# Question 1
fruits = ["apples","banana", "pear","cherry","peaches"]
for x in fruits:
    print(x)

# Question 2    
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

# Question 3
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x**2)

# Question 4
import random

colors = ["red","blue","pink","yellow","brown"]
random.shuffle(colors)
for x in colors:
    print(x)
# Question 5
import math_operations
math_operations
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
while True:
    if operation == "+":
        result = math_operations.add(input1, input2)

    elif operation == "-":
        result = math_operations.subtract(input1, input2)

    elif operation == "*":
        result = math_operations.multiply(input1, input2)

    elif operation == "/":
        result = math_operations.divide(input1, input2)
        if input2 != 0:
            print("Error Division by zero is not allowed.")
        print(result)
        break           

#Question 1: Multi-Step Arithmetic Operations
import math

a = 10
b = 5
c = 2

result1 = a + b
result2 = result1 * c
result3 = math.sqrt(result2)
print(result3)

# Question 2: Complex Conditional Evaluation
x = int(input("Enter an integer for x "))
y = int(input("Enter an integer for y "))
z = int(input("Enter an integer for z "))
if x % 2 == 0 and y > 0 and 10 < z < 50:
    print("All conditions are met.")

# Question 3: Grading with Adjustments
base_score = int(input("Enter base score: "))
bonus_points = 5
late_penalty = -10

Final_score = base_score + bonus_points + late_penalty
Final_score = max(0, min(Final_score, 100))
print("Your final score is",Final_score)

# Question 4: Advanced Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter operation (+, -, *, %, /) ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "%":
    result = num1 % num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
            result = "Error: Division by zero is not allowed."
     
print(result)
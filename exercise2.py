# Question 1: Arithmetic and Assignment Operators
x = 3
y = 2

x += 3
y *= 2

result = x / y
print(result)

# Question 2: Comparison and Logical Operators

a = 5
b = 4
c = 6

condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a

final_condition = condition1 or (condition2 and condition3)

print(final_condition)

# Question 3: Conditional Statements

score = int(input("Enter your Test score (0-100): "))

if score >= 90:
     print("A")
elif score >= 80:
     print("B")
elif score >= 70:
     print("C")
elif score >= 60:
     print("D")
else:
     print("F")


# Question 4: Combining Operators and Conditionals

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
            result = "Error: Division by zero is not allowed."
     
print(result)

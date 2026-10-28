# Question 1: Basic Function Definition and Calling
def greet():
    print("Hello world!")

greet()

# Question 2: Function with Parameters
name = "Samkele Ndzishe"
def persinalized_greeting(name):
    print(name)

persinalized_greeting(name)

# Question 3: Function with Return Value
def square(num):
   return   num ** 2
Sum_result = square(5)
print(Sum_result)

# Question 4: Function with Multiple Parameters and Return Value
def rectangle_area (length, width):
    return length * width
final_result = rectangle_area(4, 5)
print(final_result)

# Question 5: Using a Function as an Argument

def apply_operation (fun, num):
    return fun(num)
def double(num):
    return num*2
thisresult = apply_operation(double, 2) + 7
print(thisresult)

def hambur
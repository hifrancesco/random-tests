# ### functions ###
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b

# # Assigning functions to variables
# func1 = add
# func2 = subtract

# result1 = func1(5, 3)
# result2 = func2(5, 3)

# print(result1)
# print(result2) 

# # Storing functions in a list
# func_list = [add, subtract, multiply, divide]

# result3 = func_list[2](5, 3)

# print(result3)

# # Passing functions as arguments to other functions
# def operate(func, a, b):
#     return func(a, b)

# result4 = operate(add, 5, 3)
# result5 = operate(subtract, 5, 3) 

# print(result4)
# print(result5)


### functions ###
# def greet(greeting="Good morning", name="Francesco"):
#     print(greeting + ", " + name + "!")

# greet()
# greet("Good afternoon", "Bob")
# greet("Good evening", "Alice")


# ### functions ###
# def print_args(*args):
#     for arg in args:
#         print(arg)

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# def print_all(*args, **kwargs):
#     print_args(*args)
#     print_kwargs(**kwargs)

# print_all("Twitter @", "CloudFrancesco", goal="...sharing what I learn", day=14)


### functions ###
# def func():
#     n = 10
#     print("Inside the function: n =", n)

# func()
# print("Outside the function: n =", n)

# """
# Output:

# Inside the function: n = 10
# NameError: name 'n' is not defined
# """


### functions ###
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function '{func.__name__}' returned '{result}'")
#         return result
#     return wrapper

# @log_decorator
# def add_numbers(x, y):
#     return x + y

# result = add_numbers(35, 35)
# print(result)


### lambda functions ###
# square = lambda x: x**2
# result = square(5)
# print(result)


### functions ###
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_numbers(1, 2)
print("The result is:", result)
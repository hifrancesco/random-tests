### functions ###
def add_numbers(x, y, z):
    result = x + y + z
    return result

sum = add_numbers(5, 10, 15)
print(sum)

### functions ###
def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    return inner_function

def function_executor(func):
    print("Executing function:")
    func()

# Call outer function to get the inner function
inner_func = outer_function()

# Call the inner function directly
inner_func()

# Pass the inner function as an argument to another function
function_executor(inner_func)



### functions ###
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Assigning functions to variables
func1 = add
func2 = subtract

result1 = func1(5, 3)  # Calling the function through the variable
result2 = func2(5, 3)

print(result1)  # Output: 8
print(result2)  # Output: 2

# Storing functions in a list
func_list = [add, subtract, multiply, divide]

result3 = func_list[2](5, 3)  # Calling the third function in the list

print(result3)  # Output: 15

# Passing functions as arguments to other functions
def operate(func, a, b):
    return func(a, b)

result4 = operate(add, 5, 3)  # Calling operate() function with add() function as argument
result5 = operate(subtract, 5, 3)  # Calling operate() function with subtract() function as argument

print(result4)  # Output: 8
print(result5)  # Output: 2
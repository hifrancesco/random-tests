
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print ("Welcome to Calculator")
print ()

while True:
    print ("Select Operation: \n (1) Addition \n (2) Substraction \n (3) Multiplication \n (4) Division")

    operation = input("Enter your choice (1/2/3/4): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if operation == '1':
        print("Output is: ", add(num1, num2))
    elif operation == '2':
        print("Output is: ", substract(num1, num2))
    elif operation == '3':
        print("Output is: ", multiply(num1, num2))
    elif operation == '4':
        print("Output is: ", divide(num1, num2))
    else:
        print("Invalid operation")
    
    print("----")
    print()
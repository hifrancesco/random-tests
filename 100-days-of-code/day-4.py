### Arithmetic Operators ###
import random


def arithmetic():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    exponentiation = a**b
    floor_division = a // b
    for i in [
        addition,
        subtraction,
        multiplication,
        division,
        modulus,
        exponentiation,
        floor_division,
    ]:
        print("Result: " + str(i))


### Assignment Operators ###
# **= : Raises a variable to the power of a value and assigns the result to the variable.
x = 2
x **= 3
print("Result:", x)  # Output: 8

# &= : Performs a bitwise AND operation on a variable and a value, and assigns the result to the variable.
x = 10
x &= 3
print("Result:", x)  # Output: 2

# |= : Performs a bitwise OR operation on a variable and a value, and assigns the result to the variable.
x = 10
x |= 3
print("Result:", x)  # Output: 11

# ^= : Performs a bitwise XOR operation on a variable and a value, and assigns the result to the variable.
x = 10
x ^= 3
print("Result:", x)  # Output: 9

# >>= : Performs a right shift operation on a variable and a value, and assigns the result to the variable.
x = 10
x >>= 1
print("Result:", x)  # Output: 5

# <<= : Performs a left shift operation on a variable and a value, and assigns the result to the variable.
x = 10
x <<= 1
print("Result:", x)  # Output: 20

# **= : Raises a variable to the power of a value and assigns the result to the variable.
x = 2
x **= 3
print("Result:", x)  # Output: 8

# &= : Performs a bitwise AND operation on a variable and a value, and assigns the result to the variable.
x = 10
x &= 3
print("Result:", x)  # Output: 2

# |= : Performs a bitwise OR operation on a variable and a value, and assigns the result to the variable.
x = 10
x |= 3
print("Result:", x)  # Output: 11

# ^= : Performs a bitwise XOR operation on a variable and a value, and assigns the result to the variable.
x = 10
x ^= 3
print("Result:", x)  # Output: 9

# >>= : Performs a right shift operation on a variable and a value, and assigns the result to the variable.
x = 10
x >>= 1
print("Result:", x)  # Output: 5

# <<= : Performs a left shift operation on a variable and a value, and assigns the result to the variable.
x = 10
x <<= 1
print("Result:", x)  # Output: 20


### Comparison Operators ###
def comparison():
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    print(x == y)
    print(x != y)
    print(x > y)
    print(x < y)
    print(x >= y)
    print(x >= y)


### Logical Operators ###
def logical():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    print(a == b and c != d)
    print(a > b and c < d)
    print(a >= b or c <= d)
    print(a != b or c > d)


### Identity Operators ###
x = ["football", "chess", "travelling"]
y = ["football", "chess", "travelling"]
print(x is y)  # Output: False

x = ["football", "chess", "travelling"]
y = ["football", "chess", "travelling"]
print(x is not y)  # Output: True


### Membership Operators ###
countries = ["Japan", "Mexico", "Armenia", "India"]
if "Mexico" in countries:
    print("Mexico is present in the list.")

fruits = ["dragonfruit", "durian", "rambutan"]
if "grape" not in fruits:
    print("Grape is not present in the list.")


### Bitwise Operators ###
a = random.randint(1, 25)
b = random.randint(1, 25)
b = ~a
print(b)
b = a << 2
print(b)
b = a >> 1
print(b)
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
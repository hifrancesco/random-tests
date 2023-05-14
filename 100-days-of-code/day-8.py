### pdb ###
import pdb


def add(x, y):
    # setting a breakpoint
    pdb.set_trace()
    result = x + y
    return result


print(add(3, 5))


### if elif else conditional statements ###
weather = input("What's the weather like? ").strip()
temp = int(input("What's the temperature like? "))

if weather == "sunny":
    if temp > 23:
        print("Let's have some ice cream!")
    else:
        print("Let's have a salad.")
elif weather == "rainy":
    print("Let's have some warm soup.")
else:
    print("Let's have some pizza.")

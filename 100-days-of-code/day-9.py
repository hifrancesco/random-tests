### for loop ###
cities = ["Lagos", "Cairo", "Johannesburg", "Nairobi", "Casablanca"]

for index, city in enumerate(cities):
    print(f"City number {index+1} is {city}.")


### for loop ###
"""
This loop will print the numbers 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
"""
for num in range(2, 21, 2):
    print(num)


### for loop ###
vegetables = ["carrot", "broccoli", "zucchini", "tomato", "cabbage"]

print("Here are the vegetables in alphabetical order:")
for veg in sorted(vegetables):
    print(veg)


### for loop ###
n = [1, 2, 3, 4, 5]


def square(x):
    return x**2


squared_numbers = map(square, n)

for i in squared_numbers:
    print(i)


### while loop ###
x = 0
while x < 5:
    print(x)
    x += 1


### while loop ###
fruits = ["apple", "banana", "orange", "kiwi"]
eaten = []

while len(eaten) < 3:
    choice = input("What fruit would you like to eat? ").lower()
    if choice in fruits:
        print("Enjoy your", choice)
        eaten.append(choice)
    else:
        print("We don't have that fruit.")

print("You've eaten 3 fruits!")


### while loop ###
temp = 0 

while not (10 <= temp <= 20):
    temp = float(input("Temperature: "))
    
    if temp < 10:
        print("It's cold.")
    elif temp > 20:
        print("It's hot.")
    else:
        print("The temperature is just right. Enjoy your day!")


### continue, pass, break ###
numbers = [2, 3, 7, 9, 12, 14, 17, 20, 23]

for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        continue
    elif num % 3 == 0:
        pass
    elif num > 20:
        print("Greater than 20 found:", num)
        break
    else:
        print("Number found:", num)


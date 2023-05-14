### str ###
greeting = "Hello, World!"
print(greeting, "is", type(greeting))


### int, float, complex ###
a = 1
b = 1.2
c = 2j

for i in [a, b, c]:
    print(i, "is", type(i))


### list, tuple, range ###
shop_list = ["apple", "banana", "cherry"]
shop_tuple = ("kiwi", "watermelon", "lemon")
shop_range = range(10)

for i in [shop_list, shop_tuple, shop_range]:
    print(i, "is", type(i))


### dict ###
my_details = {
    "Twitter": "CloudFrancesco",
    "Challenge": "#100DaysOfCode",
    "Period": 100}

print(my_details, "is", type(my_details))


### set, frozenset ###
shop_set = {"pineapple", "papaya", "coconut"}
shop_frozenset = frozenset(shop_set)

for i in [shop_set, shop_frozenset]:
    print(i, "is", type(i))


### bool ###
cities = ["Athens", "Tokyo", "Hanoi", "Prague"]
oslo = "Oslo" not in cities
new_york = "New York" in cities

for i in [oslo, new_york]:
    print(i, "is", type(i))


### bytes, bytearray, memory ###
d = b"JavaScript"
e = bytearray(b"Java")
f = memoryview(b"C#")

for i in [d, e, f]:
    print(i, "is", type(i))


### NoneType ###
name = None
print(name, "is", type(name))
# ### lambdas ###
# double = lambda x: x * 2
# print(double(5))


# ### lambdas ###
# # sorting a list of tuples based on the second element of each tuple
# my_list = [("apple", 5), ("banana", 2), ("orange", 7), ("pear", 1)]
# sorted_list = sorted(my_list, key=lambda x: x[1])
# print(sorted_list)


# ### lambdas ###
# numbers = [5, 2, 7, 1, 9, 8, 3, 6, 4]

# # Sort the numbers in ascending order using the sorted() function and a lambda function as the key argument
# sorted_numbers = sorted(numbers, key=lambda x: x)

# # Filter out the odd numbers using the filter() function and a lambda function as the argument
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# # Map each number to its square using the map() function and a lambda function as the argument
# squared_numbers = list(map(lambda x: x ** 2, numbers))

# print(sorted_numbers)
# print(even_numbers)
# print(squared_numbers)


### lambdas ###
# double = lambda x: x * 2
# print(double(5))


# ### lambdas ###
# # sorting a list of tuples based on the second element of each tuple
# my_list = [("apple", 5), ("banana", 2), ("orange", 7), ("pear", 1)]
# sorted_list = sorted(my_list, key=lambda x: x[1])
# print(sorted_list)


### object-oriented programming ###
class Person:
    # class attribute
    name = ""
    age = 0
    height = 0
    calm = "calm"


# create person1 object
person1 = Person()
person1.name = "Tommy"
person1.age = 35
person1.height = 1.75
person1.calm = "calm"
person1.happy = "not happy"

# create another object person2
person2 = Person()
person2.name = "Mulenga"
person2.age = 31
person2.height = 1.80
person2.calm = "not calm"
person2.happy = "happy"

# access attributes
print(
    f"{person1.name} is {person1.age} years old. He is {person1.height} tall. Most of the times he is {person1.calm}, but {person1.happy}."
)
print(
    f"{person2.name} is {person2.age} years old. He is {person2.height} tall. Most of the times he is {person2.calm}, but {person2.happy}."
)
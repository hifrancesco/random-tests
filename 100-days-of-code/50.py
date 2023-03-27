### lambdas ###
double = lambda x: x * 2
print(double(5))


### lambdas ###
# sorting a list of tuples based on the second element of each tuple
my_list = [("apple", 5), ("banana", 2), ("orange", 7), ("pear", 1)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


### lambdas ###
numbers = [5, 2, 7, 1, 9, 8, 3, 6, 4]

# Sort the numbers in ascending order using the sorted() function and a lambda function as the key argument
sorted_numbers = sorted(numbers, key=lambda x: x)

# Filter out the odd numbers using the filter() function and a lambda function as the argument
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Map each number to its square using the map() function and a lambda function as the argument
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(sorted_numbers)
print(even_numbers)
print(squared_numbers)
### int(), float(), str() ###
a = int(3.14159)
b = float(10)
c = str(15)


for i in [a, b, c]:
    print(i, "is", type(i))


### implicit type conversion ###
int_num = 5
float_num = 2.5
new_number = int_num + float_num

print("Value:", new_number)
print("Data type of new_number:", type(new_number))


### explicit type conversion ###
string_num = '10'
int_num = 23

print("Data type of string_num before casting:", type(string_num))
string_num = int(string_num)

print("Data type of string_num after casting:", type(string_num))
num_sum = int_num + string_num

print("Value:", num_sum)
print("Data type of num_sum:", type(num_sum))
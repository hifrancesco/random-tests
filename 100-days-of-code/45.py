# import os

# # Join two path components into a complete path
# path = os.path.join("/Users", "francescowang/Desktop", "example.txt")
# print(path) # Output: /home/user/example.txt

# # Get the directory name from a path
# dir_name = os.path.dirname(path)
# print(dir_name) # Output: /home/user

# # Get the file name from a path
# file_name = os.path.basename(path)
# print(file_name) # Output: example.txt

# # Check if a path exists
# print(os.path.exists(path)) # Output: False

# # Create a directory if it doesn"t exist
# if not os.path.exists(dir_name):
#     os.makedirs(dir_name)

# # Create a file
# with open(path, "w") as f:
#     f.write("Hello, world!")

# # Check if the file exists
# print(os.path.exists(path)) # Output: True

# # Read the contents of the file
# with open(path, "r") as f:
#     contents = f.read()
#     print(contents) # Output: Hello, world!


### file handling using the os module ###
import os

path = os.path.join("/Users", "cloudfrancesco/Desktop", "example.txt")
print(path)

dir_name = os.path.dirname(path)
print(dir_name)

file_name = os.path.basename(path)
print(file_name)
print(os.path.exists(path))

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

with open(path, "w") as f:
    f.write("Follow me on Twitter @CloudFrancesco.")

print(os.path.exists(path))
with open(path, "r") as f:
    contents = f.read()
    print(contents)
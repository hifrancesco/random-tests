### file handling ###
file = open("example.txt", "r")
contents = file.read()
print(contents)
file.close()


### file handling ###
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
    
"""
The built-in open() function is used to open a file and returns a file object. 

The syntax for opening a file is open(filename, mode).
where filename is a string representing the name or path of the file, and mode is a string representing the mode in which the file should be opened (e.g. "r" for read mode, "w" for write mode, etc.).

"""



### file handling ###
file = open("file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()


### file handling ###
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
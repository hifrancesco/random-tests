Variables are reserved memory locations to store values in order to store some type of value.

Data type is an important concept. Variables can store data of different types, and different types can do different things.



# def greet(name):
#     if name is not None:
#         print("This is " + name + "!")
#     else:
#         print("Follow me for awesome content.")
        
# greet("CloudFrancesco")
# greet(None)



The built-in `open()` function is used to open a file and returns a file object. 

The syntax for opening a file is `open(filename, mode)`.

The filename is a string representing the name or path of the file.

The mode is a string representing the mode in which the file should be
opened (e.g. `'r'` for read mode, `'w'` for write mode, etc.).



Python provides several methods for reading data from a file object:

- `read()` reads the entire contents of a file as a string.
- `readline()`  reads a single line of the file.
- `readlines()` reads all lines of the file and returns them as a list.


Python provides several methods for writing data to a file object:

- `write()` writes a string to the file.
- `writelines()` writes a list of strings to the file
- `print()` function can also be used to write data to a file by specifying the file parameter.




When working with files, it is important to close the file object when you are done using it to free up system resources. 

- You can close a file object using the `close()` method.

Python also provides a with statement for working with files, which automatically takes care of closing the file when you are done using it. 

- The syntax for using a with statement with a file object is

`with open(filename, mode) as file:`

Within the block of the `with` statement, you can perform any file operations you need to, and the file will automatically be closed when you exit the block.




Python allows you to work with file paths and directories using the `os` and `os.pat`h modules. 

The `os` module provides methods for interacting with the file system, while the `os.path` module provides methods for manipulating file paths.

Python also provides a `pickle` module for serializing and de-serializing objects to and from files. 

This can be useful for storing and retrieving complex data structures, such as lists, dictionaries, and objects.




An object is any entity that has attributes and behaviors. For example, a person is an object.

- attributes - name, age, height, etc.
- behaviour - calm, happy, etc.

Similarly, a class is a blueprint for that object.

class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")



The `__init__` method is used to initialize the width and height attributes of a rectangle object. 

These attributes are passed in as parameters when an instance of the Rectangle class is created. 

The area and perimeter methods use these attributes to calculate the area and perimeter of the rectangle.

You can create an instance of the Rectangle class by passing the width and height as arguments to the constructor `__init__` method.

You can call the methods `area()` and `perimeter()` on the instance to get the area and perimeter of the rectangle.
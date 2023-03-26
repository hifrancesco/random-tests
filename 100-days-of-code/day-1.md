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
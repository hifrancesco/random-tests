# ### object-oriented programming ###
# """
# The self is used in both the constructor method (__init__) and the square method. 

# In __init__, self refers to the instance of the class that's being created, and number is an argument that's used to initialize one of the instance's attributes (self.number).

# In square, self again refers to the instance, and self.number is used to compute the square of the instance's number attribute.

# """


# class SquareN:
#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         return self.number**2


# """
# When you create an instance of SquareN, you don't need to pass in the self parameter explicitly.

# Python does this for you behind the scenes. For example:

# """

# calc = SquareN(10)
# print(calc.square())

# """
# calc is an instance of SquaredN, and calc is passed as an argument to the constructor.

# When the square method is called on calc, self is automatically set to calc, so self.number refers to calc.number, which is 10.

# The method computes and returns the square of 10, which is 100.

# """
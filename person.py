### object-oriented programming ###
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age}.")
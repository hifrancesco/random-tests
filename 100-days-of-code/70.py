### object-oriented programming ###
"""
The base class iscalled Animal which has an __init__ method that takes a name parameter, 
and a speak method that just prints "Animal sound".

We also have two derived classes, Dog and Cat, which inherit from Animal.
They both have their own speak method that overrides the speak method of the base class.

Finally, we create an instance of Dog called dog with the name "Charlie",
and an instance of Cat called cat with the name "Garfield". 

We call the speak method on both of them, and they output "Woof!" and "Meow!" respectively, 
which are the sounds that we defined for each class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Charlie")
cat = Cat("Garfield")

dog.speak()
cat.speak()
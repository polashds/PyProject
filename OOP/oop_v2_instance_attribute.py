'''
To define and initialize an attribute for all instances of a class, 
you use the __init__ method. '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The following creates a Person object named person:
person = Person("Alice", 25)

# To access an instance attribute, you use the dot notation.
print(person.name)
print(person.age)
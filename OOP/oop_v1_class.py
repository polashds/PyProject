# class as a blueprint (like a recipe or a template)
# object has a state and behaviors.
# object is an instance of a class
# define a class first to create an object from it
# from the class, you can create one or more objects.
# To create an object from the Person class, use the class name followed by parentheses (), like calling a function
# person = Person() the 'person' is an instance of the 'Person' class.
# Object / Instance: When you use the class to make something, you create an instance (an actual object).
# A class is a template for creating objects, while an object is an instance of a class.
# Attributes are the data that belong to the object. 
# Methods are the actions that the object can perform.
# Methods are functions inside the class that objects can use.
# analogy: class as blueprint → object as product → attributes as features/properties → methods as actions)
# Object and Instance are essentially the same thing.
# But the difference is in how we talk about them
# We use the word instance when we want to emphasize that it was created from a class.
# We use the word object more generally: anything created in Python is an object.
# Every instance is an object. But not every object is an instance of your custom class

# Instance Attributes: self.name = name 
# A. Belong to each individual object (instance).
# B. Defined in the __init__ method using self.

# Class Attributes: class Dog:
    #species = "Canis familiaris"   # class attribute
# Belong to the class itself, not to any specific instance.
# They are shared by all instances of the class.
# They are defined in the class body outside the __init__ method.

# Instance Methods:
# Functions that belong to the class, but work on an instance (object).
#Always take self as the first parameter (so they know which object they are working with).

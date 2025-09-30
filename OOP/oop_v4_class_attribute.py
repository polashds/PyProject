'''
Unlike instance attributes, class attributes are shared by all instances 
of the class. They are helpful if you want to define class constants 
or variables that keep track of the number of instances of a class.
'''

class Person:
    counter = 0 # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        return f'Hi, its {self.name}'
    
# access the counter attribute from the Person class:
print(Person.counter)

# Or from any instances of the Person class:
person1 = Person('Alice', 25)
person2 = Person('Bob', 30)
print(person1.counter)
print(person2.counter)


'''
To make the counter variable more useful, 
you can increase its value by one once an object is created. 
To do it, you increase the counter class attribute in the __init__ method
'''

class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."
    
# The following creates two instances of the Person class and shows the value of the counter
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(Person.counter)
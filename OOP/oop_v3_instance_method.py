class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hi, its {self.name}'
        

# To call an instance method, you also use the dot notation.
person = Person("Alice", 25)
print(person.greet())
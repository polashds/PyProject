'''
Like a class attribute, a class method is shared by all instances of the class.
The first argument of a class method is the class itself. 
By convention, its name is 'cls'. Python automatically passes this argument 
to the class method. Also, you use the @classmethod decorator to decorate a
class method.
'''

class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f'Hi, its {self.name}'
    
    @classmethod
    def create_anonymous(cls):
        return Person("Anonymous", 11)
       

# calling the class method
anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous

# calling the instance method
# person = Person("Alice", 25)
# print(person.greet())

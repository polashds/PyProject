class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hi, its {self.name}'

'''
A class can reuse another class by inheriting it. 
When a child class inherits from a parent class, 
the child class can access the attributes and methods of the parent class.
'''


class Employee(Person):
    def __init__(self, name, age, job_title):
        #super() calls the parent (Person) __init__ to set name and age
        super().__init__(name, age)

        # add a new attribute only for Employee
        self.job_title = job_title

'''
Inside the __init__ method of the Employeemclass, super(). calls the __init__ 
method of the Person class to initialize the name and age attributes.
'''
# The super() allows a child class to access a method of the parent class.
# The Employee class extends the Person class by adding one more attribute 
# called job_title.

# To override the greet() method in the Person class, 
# you can define the greet() method in the Employee class as follows:

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f", my job title is {self.job_title}"
    

'''
The greet() method in the Employee is also called the greet() method
 of the Person class. In other words, it delegates to a method of the
 parent class.
'''

# The following creates a new instance of the Employee class 
# and call the greet() method:

employee = Employee("Polash", 25, "Python Developer")
print(employee.greet())



# # easier version without using super()
# class Employee:
#     def __init__(self, name, age, job_title):
#         self.name = name       # set name
#         self.age = age         # set age
#         self.job_title = job_title  # set job title
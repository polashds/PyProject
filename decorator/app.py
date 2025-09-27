def say_hello():
    print("Hello")

def my_decorator(func):
    def wrapper():
        print("Before opening the gift")
        func()
        print("after opening the gift")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")

say_hello()
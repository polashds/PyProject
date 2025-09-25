def my_decorator(func):
    def wrapper(*arg, **kwargs):
        print("before opening the gift")
        func(*arg, **kwargs)
        print("after opening the gift")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Polash")
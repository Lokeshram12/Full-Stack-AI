from functools import wraps
def my_decorator(func):
    @wraps(func)  # used to preserve the existing metadata
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


@my_decorator

def hello():
    print("Hello world")

hello()

print(hello.__name__)
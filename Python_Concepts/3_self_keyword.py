class Chaicup:
    size = 150

    def __init__(self,type_,size):  # Constructor with parameters

        # Use of '__init__' method to initialize instance variables - this is a

        self.type = type_
        self.size = size

    def describe(self):
        return f"This chaicup is {self.size}ml in size."
    
    def summary(self):
        return f"This is a {self.type} chaicup of size {self.size}ml."


my_chaicup = Chaicup("Masala", 150)

print(my_chaicup.describe()) # Output: This chaicup is 150ml in size.

print(Chaicup.describe(my_chaicup)) # Output: This chaicup is 150ml in size.

# print(Chaicup.describe())   # This will raise a TypeError because 'self' is not provided


print(my_chaicup.summary()) # Output: This is a Masala chaicup of size 150ml.



# Compostion vs Inheritance

# Composition Example
class Engine:
    def start(self):
        return "Engine started"
class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine (composition)
    def start_car(self):
        return self.engine.start()

my_car = Car()
print(my_car.start_car())  # Output: Engine started

# Inheritance Example
class Vehicle:
    def start(self):
        return "Vehicle started"
class Bike(Vehicle):  # Bike inherits from Vehicle
    pass    
my_bike = Bike()
print(my_bike.start())  # Output: Vehicle started

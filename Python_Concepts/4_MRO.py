# Method Resolution Order (MRO) in Python

# MRO is the order in which Python looks for a method in a hierarchy of classes.
class A:
    def show(self):
        return "Method from class A"
class B(A):
    def show(self):
        return "Method from class B"
class C(A):
    def show(self):
        return "Method from class C"
class D(B, C):
    pass    
my_object = D()
print(my_object.show())  # Output: Method from class B

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
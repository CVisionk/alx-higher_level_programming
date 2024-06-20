#/!usr/bin/env python3
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Class:", cls)

# You can call the class method without creating an instance
MyClass.class_method()

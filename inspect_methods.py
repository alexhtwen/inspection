import inspect
import sys

from tools import say

class Bacteria:
    def instance_method(self):
        """This is an instance method in Bacteria."""
        ...

    @classmethod
    def class_method(cls):
        """This is a class method in Bacteria."""
        ...

    @staticmethod
    def static_method1():
        """This is a static method in Bacteria."""
        ...

    @staticmethod
    def static_method2():
        """This is another static method in Bacteria."""
        ...

class Plant:
    def instance_method(self):
        """This is an instance method in Plant."""
        ...

    @classmethod
    def class_method1(cls):
        """This is the first class method in Plant."""
        ...

    @classmethod
    def class_method2(cls):
        """This is the second class method in Plant."""
        ...

    @classmethod
    def class_method3(cls):
        """This is the third class method in Plant."""
        ...

class Animal:
    def instance_method1(self):
        """This is an instance method in Animal."""
        ...

    def instance_method2(self):
        """This is another instance method in Animal."""
        ...

    @staticmethod
    def static_method():
        """This is a static method in Animal."""
        ...

def get_all_methods(cls):
    """
    Returns a dictionary categorizing all methods of the class into
    instance methods, class methods, and static methods.
    """
    methods = {
        'instance_methods': [],
        'class_methods': [],
        'static_methods': []
    }

    # Iterate through all members of the class
    for name, obj in inspect.getmembers(cls):
        # Check if it's an instance method or class method
        if inspect.isfunction(obj):
            # Check if the method is a staticmethod using the class's __dict__
            if isinstance(cls.__dict__.get(name), staticmethod):
                methods['static_methods'].append(name)
            else:
                methods['instance_methods'].append(name)
        elif inspect.ismethod(obj):
            methods['class_methods'].append(name)

    return methods

def get_all_classes(module):
    """
    Returns a list of all classes defined in the given module.
    """
    return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if cls.__module__ == module.__name__]


# Example usage
if __name__ == "__main__":
    # Dynamically get the current module
    current_module = sys.modules[__name__]   # 目前模組
    print()
    # for name, obj in inspect.getmembers(Bacteria(), predicate=inspect.ismethod):
    #     print(name, obj)
    # print()
    # for name, obj in inspect.getmembers(Bacteria(), predicate=inspect.isfunction):
    #         print(name, obj)
    # print()

    # print()
    # for name, obj in inspect.getmembers(ExampleClass, predicate=inspect.ismethod):
    #     print(name, obj)




    # # Dynamically list all classes in the current module
    classes_and_methods = {
        cls.__name__: get_all_methods(cls)
        for cls in get_all_classes(current_module)
    }

    for class_name, methods in classes_and_methods.items():
        print(f"Class: {class_name}")
        print(f"  Instance Methods: {methods['instance_methods']}")
        print(f"  Class Methods   : {methods['class_methods']}")
        print(f"  Static Methods  : {methods['static_methods']}")
        print()
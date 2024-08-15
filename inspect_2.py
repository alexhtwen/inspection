import inspect

class ExampleClass:
    def instance_method(self):
        """This is an instance method."""
        pass

    @classmethod
    def class_method(cls):
        """This is a class method."""
        pass

    @staticmethod
    def static_method():
        """This is a static method."""
        pass


# Inspect the class itself
for name, obj in inspect.getmembers(ExampleClass, predicate=[inspect.isfunction, inspect.ismethod]):
    print(name, obj)
print()
for name, obj in inspect.getmembers(ExampleClass, predicate=inspect.ismethod):
    print(name, obj)

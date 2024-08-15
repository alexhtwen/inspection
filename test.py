import inspect

class ExampleClassA:
    def instance_method(self):
        """This is an instance method in ExampleClassA."""
        pass

    @classmethod
    def class_method(cls):
        """This is a class method in ExampleClassA."""
        pass

    @staticmethod
    def static_method():
        """This is a static method in ExampleClassA."""
        pass

class ExampleClassB:
    def another_instance_method(self):
        """This is an instance method in ExampleClassB."""
        pass

    @staticmethod
    def another_static_method():
        """This is a static method in ExampleClassB."""
        pass

def list_classes_and_methods(module):
    """
    Lists all classes in the given module and categorizes their methods.
    """
    classes_info = {}

    # Inspect all classes in the module
    for name, cls in inspect.getmembers(module, predicate=inspect.isclass):
        methods = {
            'instance_methods': [],
            'class_methods': [],
            'static_methods': []
        }

        # Iterate through all members of the class
        for method_name, method_obj in inspect.getmembers(cls):
            if inspect.isfunction(method_obj):
                # Differentiate static methods from instance methods
                if isinstance(getattr(cls, method_name), staticmethod):
                    methods['static_methods'].append(method_name)
                else:
                    methods['instance_methods'].append(method_name)
            elif inspect.ismethod(method_obj):
                # Class methods are bound methods at the class level
                methods['class_methods'].append(method_name)

        classes_info[name] = methods

    return classes_info

# Example usage
if __name__ == "__main__":
    import sys
    # List all classes and their methods in the current module
    classes_and_methods = list_classes_and_methods(sys.modules[__name__])

    for class_name, methods in classes_and_methods.items():
        print(f"Class: {class_name}")
        print(f"  Instance Methods: {methods['instance_methods']}")
        print(f"  Class Methods: {methods['class_methods']}")
        print(f"  Static Methods: {methods['static_methods']}")
        print()

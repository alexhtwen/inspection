import inspect
import sys

class Tree:
    def instance_method(self):
        """This is an instance method."""
        ...

    @classmethod
    def class_method(cls):
        """This is a class method."""
        ...

    @staticmethod
    def static_method():
        """This is a static method."""
        ...


def foo():
    ...

def boo():
    ...

name = 'Alex'
age = 39
weight = 69.3
is_vegan = False
alias = ('老溫', '溫大哥', '朱V')
family = {'spouse': 'Marrianne', 'children': ['Rebecca', 'Thomas']}
# Create an instance of the class
tree = Tree()
# List of objects to check
tree_objs_to_check = (
    tree.instance_method,   # Bound instance method
    Tree.class_method,      # Bound class method
    Tree.static_method,     # Static method
)

# 用dir()可列出目前module的objects
print('Using dir():\n----------------')
print(dir())
# -----------
# 以下練習用inspect module
print('\nUsing inpect module:\n----------------')
current_module = sys.modules[__name__]

# 列出目前module的所有objects
print('\nList all objects within this module: ')
for name, obj in inspect.getmembers(current_module):
    print(name, obj)

print('\nList functions: ')
# 只列目前module的functions(函數)
for name, obj in inspect.getmembers(current_module, predicate=inspect.isfunction):
    print(name, obj)

print('\nList classes:')
# 只列目前module的classes(類別)
for name, obj in inspect.getmembers(current_module, predicate=inspect.isclass):
    print(name, obj)

print('\nList methods(not including static methods):')
# 只列目前module的instance methods和class methods(方法)
for name, obj in inspect.getmembers(Tree, predicate=inspect.ismethod):
    print(name, obj)

print('\nList methods(including static methods):')
# 只列目前module的methods(方法)
for name, obj in inspect.getmembers(Tree, predicate=inspect.isfunction):
    print(name, obj)

# Check each object using inspect.ismethod()
print('\nCheck each object using inspect.ismethod():')
for tree_obj in tree_objs_to_check:
    is_method = inspect.ismethod(tree_obj)
    is_function = inspect.isfunction(tree_obj)
    print(f"Object: {tree_obj.__name__}\t {is_method=}\t {is_function=}")




import inspect

class ExampleClass:
    def instance_method(self):
        """This is an instance method."""
        ...

    @classmethod
    def class_method(cls):
        """This is a class method."""
        ...

    @staticmethod
    def static_method():
        """This is a static method."""
        ...


# Create an instance of the class
example_instance = ExampleClass()

for name, obj in inspect.getmembers(example_instance, predicate=inspect.ismethod):
    print(name, obj)

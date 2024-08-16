import inspect
import sys

def foo():
    def __init__():
        print('hello')

def boo():
    ...

name = 'Alex'
age = 39
weight = 69.3
is_vegan = False
alias = ('老溫', '溫大哥', '朱V')
family = {'spouse': 'Marrianne', 'children': ['Rebecca', 'Thomas']}


# 用dir()可列出目前module的objects
print('Using dir():\n----------------')
print(dir())
# -----------
# 以下練習用inspect module
print('\nUsing inpect module:\n----------------')
current_module = sys.modules[__name__]

# # 列出目前module的所有objects
# print('\nList all objects within this module: ')
# for name, obj in inspect.getmembers(current_module):
#     print(name, obj)

# print('\nList functions: ')
# 只列目前module的functions(函數)
for name, obj in inspect.getmembers(current_module, predicate=inspect.isfunction):
    print(name, obj, obj.co_firstlineno)

# print('\nList classes:')
# # 只列目前module的classes(類別)
# for name, obj in inspect.getmembers(current_module, predicate=inspect.isclass):
#     print(name, obj)

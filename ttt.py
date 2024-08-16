import inspect
import sys
import random as rd
import re

def test(x: int):
    for _ in range(x):
        print('Hello, world')
        # comment
    return x ** 2

# 目前module
test_source = inspect.getsource(test)
# current_module = sys.modules[__name__]
# print(inspect.getmembers(current_module))

test_source = inspect.getsource(re)

with open('./test_source.py', 'w') as f:
    f.write(test_source)
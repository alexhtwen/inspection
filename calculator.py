# import inspect

# # class Calculator():
# #     def __init__(self, operant1: int | float, operator: str):
# #         ...

# def test_addition():
#     assert 1 + 1 == 2

# def test_subtraction():
#     assert 2 - 1 == 1

# def run_tests():
#     print('aaaaaaaa')
#     for name, obj in inspect.getmembers(inspect.stack()[1][0]):
#         print(name)
#         if name.startswith('test_') and inspect.isfunction(obj):
#             print('bbbbbbbbbb')
#             try:
#                 obj()
#                 print(f"{name} passed")
#             except AssertionError:
#                 print(f"{name} failed")

# # Running the test framework

# run_tests()




import inspect

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def run_tests():
    for name, obj in inspect.getmembers(module):
        if name.startswith('test_') and inspect.isfunction(obj):
            try:
                obj()
                print(f"{name} passed")
            except AssertionError:
                print(f"{name} failed")

# Running the test framework
run_tests()

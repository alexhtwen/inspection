import inspect
from typing import Callable, Any

from tools import say
from operations import ArithmeticOperations, valid_methods, valid_operators, parse_expr

class Calculator:
    def __init__(self):
        self.operations_instance = ArithmeticOperations()
        # self.operations_instance = operations
        self.operations = self._discover_operations()

    def _discover_operations(self) -> dict[str, Callable[[int, int], int]]:
        """
        Dynamically discover and return a dictionary of supported operations.
        """

        operations = {}
        for name, func in inspect.getmembers(self.operations_instance, predicate=inspect.ismethod):
            # say(name, func)
            if name in valid_methods:
                sig = inspect.signature(func)
                doc = inspect.getdoc(func)
                operations[valid_methods[name]] = {
                    'function': func,
                    'signature': sig,
                    'doc': doc
                }
        # say(operations)
        return operations

    def calculate(self, expression: str) -> int:
        """
        Perform the calculation based on the operator and operands.
        """

        return_value = None
        operand1, operator, operand2 = parse_expr(expression, valid_operators)
        # say(operand1, operator, operand2)
        operation = ArithmeticOperations()
        if operator in self.operations:
            func_info = self.operations[operator]
            func = func_info['function']
            say(func.__name__, func_info['signature'], func_info['doc'])
            # print(f"Signature: func_info['signature'], func_info['doc']")
            # print(f"Documentation: {func_info['doc']}")
            return func(operand1, operand2)
        else:
            raise ValueError(f"Unsupported operator: {operator}")




# class Calculator:
#     def __init__(self, operations: Any):
#         self.operations_instance = operations
#         self.operations = self._discover_operations()

#     def _discover_operations(self) -> dict[str, Callable[[float, float], float]]:
#         """
#         Dynamically discover and return a dictionary of supported operations.
#         """
#         operator_map = {
#             'add': '+',
#             'subtract': '-',
#             'multiply': '*',
#             'divide': '/',
#         }

#         operations = {}
#         for name, func in inspect.getmembers(self.operations_instance, predicate=inspect.ismethod):
#             if name in operator_map:
#                 sig = inspect.signature(func)
#                 doc = inspect.getdoc(func)
#                 operations[operator_map[name]] = {
#                     'function': func,
#                     'signature': sig,
#                     'doc': doc
#                 }

#         return operations

#     def calculate(self, operator: str, operand1: float, operand2: float) -> float:
#         """
#         Perform the calculation based on the operator and operands.
#         """
#         if operator in self.operations:
#             func_info = self.operations[operator]
#             func = func_info['function']
#             print(f"Using function: {func.__name__}")
#             print(f"Signature: {func_info['signature']}")
#             print(f"Documentation: {func_info['doc']}")
#             return func(operand1, operand2)
#         else:
#             raise ValueError(f"Unsupported operator: {operator}")

# # Example usage
# if __name__ == "__main__":
#     # Instantiate the ArithmeticOperations class
#     arithmetic_operations = ArithmeticOperations()

#     # Create an instance of the Calculator, passing the ArithmeticOperations instance
#     calculator = Calculator(arithmetic_operations)

#     # Example inputs
#     operator = '+'
#     operand1 = 10
#     operand2 = 5

#     result = calculator.calculate(operator, operand1, operand2)
#     print(f"{operand1} {operator} {operand2} = {result}")

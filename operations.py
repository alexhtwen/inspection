import random as rd

from tools import say

# # 這個檔案的code是senior developer寫的。
class ArithmeticOperations():
    def add(self, operand1: int, operand2: int) -> int:
        """Add two numbers."""
        return operand1 + operand2

    def subtract(self, operand1: int, operand2: int) -> int:
        """Subtract second number from first."""
        # say(type(operand1), type(operand2))
        return operand1 - operand2

    def multiply(self, operand1: int, operand2: int) -> int:
        """Multiply two numbers."""
        return operand1 * operand2

    def divide(self, operand1: int, operand2: int) -> int:
        """Divide first number by second. Raises ValueError if second number is zero."""
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2

    def int_divide(self, operand1: int, operand2: int) -> int:
        """Integer divide first number by second. Raises ValueError if second number is zero."""
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 // operand2

    def power(self, operand1: int, operand2: int) -> int:
        """Multiply two numbers."""
        return operand1 ** operand2

def parse_expr(expression: str, valid_operators: dict) -> tuple:
    # print('----------------')
    operand1, operator, operand2 = 0, '', 0
    for valid_operator in valid_operators:
        if valid_operator in expression:
            partitioned_exp = expression.partition(valid_operator)
            # say(partitioned_exp)
            operand1 = int(partitioned_exp[0])
            operator = partitioned_exp[1]
            operand2 = int(partitioned_exp[2])
            break
    # say(operand1, operator, operand2)
    if operator not in valid_operators:
            raise ValueError("Invalid operator")

    return operand1, operator, operand2


operation = ArithmeticOperations()
# a dictionary mapping operators to functions
valid_operators = {   # 缺點：有順序問題
    '//': operation.int_divide,  # 要在'/'之前
    '/': operation.divide,
    '**': operation.power,       # 要在'*'之前
    '*': operation.multiply,
    '+': operation.add,
    '-': operation.subtract,    # 要放在最後
}

valid_methods = {
    'add': '+',
    'subtract': '-',
    'multiply': '*',
    'divide': '/',
    'int_divide': '//',
    'power': '**',
}

from tools import say

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

operation = ArithmeticOperations()
# a dictionary mapping operators to functions
valid_operators = {
    '//': operation.int_divide,
    '/': operation.divide,
    '**': operation.power,
    '*': operation.multiply,
    '+': operation.add,
    '-': operation.subtract,
}

valid_methods = {
    'add': '+',
    'subtract': '-',
    'multiply': '*',
    'divide': '/',
}
import random as rd

from tools import say
from operations import ArithmeticOperations, valid_operators, parse_expr


# 這個class是junior developer寫的。
class Calculator():
    def __init__(self):
        ...

    def calculate(self, expression: str) -> int:
        return_value = None
        operand1, operator, operand2 = parse_expr(expression, valid_operators)

        operation = ArithmeticOperations()
        match operator:
            case '+':
                return_value = operation.add(operand1, operand2)
            case '-':
                return_value = operation.subtract(operand1, operand2)
            case '*':
                return_value = operation.multiply(operand1, operand2)
            case '/':
                if operand2 == 0:
                    # raise ValueError("Cannot divide by zero")
                    return_value = 'Exception: Cannot divide by zero'
                else:
                    return_value = operation.divide(operand1, operand2)

        return return_value

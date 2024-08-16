from operations import ArithmeticOperations, valid_operators, parse_expr

# 這個class是junior developer寫的。
class Calculator():
    def __init__(self):
        ...

    def calculate(self, expression: str) -> int:
        return_value = None
        operand1, operator, operand2 = parse_expr(expression, valid_operators)

        operation = ArithmeticOperations()
        func = valid_operators[operator]
        return func(operand1, operand2)
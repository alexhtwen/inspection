import inspect
import ast
from typing import Any, List, Tuple

def extract_call_args(source: str) -> List[str]:
    """Extract the argument expressions from the function call source code."""
    tree = ast.parse(source)
    call = tree.body[0].value  # Assumes the first statement is the function call
    return [ast.unparse(arg) for arg in call.args]

def say(*args: Any, sep: str = '-', leng: int = 30, blank_lines: tuple = (0, 1)) -> None:
    # Get the caller's local variables and source code
    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals
    caller_source = inspect.getframeinfo(frame).code_context[0].strip()

    # Extract the argument expressions
    arg_expressions = extract_call_args(caller_source)

    # Create a list to store the argument names in the order they appear in args
    ordered_args: List[Tuple[str, Any]] = []

    for arg, expr in zip(args, arg_expressions):
        if expr in local_vars and local_vars[expr] is arg:
            ordered_args.append((expr, arg))
        elif expr.startswith("'") and expr.endswith("'") or expr.startswith('"') and expr.endswith('"'):
            # For string literals, remove quotes and don't repeat the value
            ordered_args.append((expr[1:-1], None))
        else:
            # Evaluate the expression in the context of local_vars
            try:
                value = eval(expr, globals(), local_vars)
                if value == arg:
                    ordered_args.append((expr, value))
                else:
                    ordered_args.append((expr, None))
            except:
                ordered_args.append((expr, None))

    # Print the output in the required format
    print('\n' * blank_lines[0] + f'{sep*leng}')
    for key, value in ordered_args:
        if value is not None:
            print(f'{key} = {value}')
        else:
            print(f'{key}')
    print(f'{sep*leng}' + '\n' * blank_lines[1])

    return None
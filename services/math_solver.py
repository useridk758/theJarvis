import ast
import operator as op

# Supported AST operators for safe evaluation
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}

def solve_math(expression: str):
    """
    Safely evaluate a math expression using AST only.
    Returns a number or None if invalid/unsafe.
    """
    try:
        cleaned = ''.join(c for c in expression if c in '0123456789+-*/.() ')
        tree = ast.parse(cleaned, mode='eval')
        return _eval_node(tree.body)
    except Exception:
        return None

def _eval_node(node):
    if isinstance(node, ast.Constant):          # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
    elif isinstance(node, ast.Num):             # Python <3.8
        return node.n
    elif isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](_eval_node(node.operand))
    else:
        raise TypeError(f'Unsupported type: {type(node)}')

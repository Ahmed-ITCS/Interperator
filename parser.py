class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Store the value (e.g., number, operator, or string).
        self.left = left  # Left child (for binary operations).
        self.right = right  # Right child (for binary operations).

class PrintNode:
    def __init__(self, expr):
        self.expr = expr  # Store the expression to print.

def parse_expression(tokens):
    if tokens[0][0] == "PRINT":
        tokens.pop(0)  # Remove 'print'
        tokens.pop(0)  # Remove '('
        expr = parse_term(tokens)  # Parse the content inside parentheses
        tokens.pop(0)  # Remove ')'
        return PrintNode(expr)  # Return a PrintNode

    return parse_term(tokens)

def parse_term(tokens):
    token = tokens.pop(0)
    if token[0] == "NUMBER":
        return ASTNode(int(token[1]))  # Return a node with the number
    elif token[0] == "STRING":
        return ASTNode(token[1][1:-1])  # Remove quotes and store the string
    elif token[0] == "LPAREN":
        expr = parse_expression(tokens)  # Parse inside parentheses
        return expr
    raise SyntaxError("Unexpected token")

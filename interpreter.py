from lexer import lex
from parser import parse_expression, PrintNode

class Interpreter:
    def eval(self, node):
        if isinstance(node, PrintNode):
            result = self.eval(node.expr)  # Evaluate the expression or string
            print(result)  # Print the result
            return

        if isinstance(node.value, int):
            return node.value  # Return numbers as-is

        if isinstance(node.value, str):
            return node.value  # Return strings as-is

        left_value = self.eval(node.left)
        right_value = self.eval(node.right)

        if node.value == "+":
            return left_value + right_value
        elif node.value == "*":
            return left_value * right_value
        else:
            raise ValueError(f"Unknown operator: {node.value}")

def evaluate_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    interpreter = Interpreter()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        print(f"Evaluating: {line}")
        try:
            tokens = lex(line)
            ast = parse_expression(tokens)
            interpreter.eval(ast)
        except SyntaxError as e:
            print(f"Syntax Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    evaluate_file("input.txt")

import re

# Add a pattern to recognize strings (text inside quotes)
token_specification = [
    ("NUMBER", r"\d+"),         # Integer number
    ("PLUS", r"\+"),            # Addition operator
    ("MULT", r"\*"),            # Multiplication operator
    ("LPAREN", r"\("),          # Left parenthesis
    ("RPAREN", r"\)"),          # Right parenthesis
    ("PRINT", r"print"),        # Print command
    ("STRING", r'"[^"]*"'),     # String literal inside double quotes
    ("WHITESPACE", r"\s+"),     # Ignore whitespace
]

def lex(code):
    tokens = []
    pos = 0

    while pos < len(code):
        match = None
        for token_type, pattern in token_specification:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                if token_type != "WHITESPACE":
                    tokens.append((token_type, match.group(0)))
                pos = match.end(0)
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]}")
    return tokens

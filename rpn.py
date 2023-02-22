

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calculate(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^": # exponentiation operator
        return operand1 ** operand2
    else:
        raise NotImplementedError("Unsupported operator: {}".format(operator))


def postfix_eval(expression):
    operators = ["+", "-", "*", "/", "^"]
    operand_stack = Stack()
    token_list = expression.split(" ")

    for token in token_list:
        # Check is the token is an operator or an operand!
        if token in operators:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = calculate(token, operand1, operand2)
            operand_stack.push(result)
        else:  # Toke is an Operand
            operand_stack.push(float(token))

    return operand_stack.pop()



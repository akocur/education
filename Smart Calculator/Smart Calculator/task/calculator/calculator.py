from collections import deque


def main():
    smart_calculator = SmartCalculator()
    answer = input().strip()
    while answer != '/exit':
        smart_calculator.handle(answer)
        answer = input().strip()
    print('Bye!')


class SmartCalculator:
    order_of_operators = {'-': 0, '+': 0, '=': 0, '(': 3, ')': 3, '*': 1, '/': 1, '^': 2}

    def __init__(self):
        self.result = 0
        self.postfix = deque()
        self.variables = dict()
        self.need_to_print = True
        self.operation_stack = []
        self.actions = {'+': self.add,
                        '-': self.subtract,
                        '*': self.multiply,
                        '/': self.divide,
                        '=': self.assign,
                        '^': self.pow}

    def get_operands(func):
        def wrapper(*args):
            self = args[0]
            operand_2 = self.get_value(self.operation_stack.pop())
            operand_1 = self.get_value(self.operation_stack.pop())
            if operand_1 is None or operand_2 is None:
                return False
            func(self, operand_1, operand_2)
            return True

        return wrapper

    @get_operands
    def add(self, operand_1, operand_2):
        self.operation_stack.append(operand_1 + operand_2)

    def assign(self):
        operand_2 = self.get_value(self.operation_stack.pop())
        operand_1 = self.operation_stack.pop()
        if operand_2 is None:
            return False
        if not SmartCalculator.is_correct_variable(operand_1):
            self.result = 'Invalid assignment'
            return False
        self.variables[operand_1] = operand_2
        self.operation_stack.append(operand_1)
        self.need_to_print = False
        return True

    def calculate(self):
        self.result = 0
        self.need_to_print = True
        self.operation_stack.clear()
        while self.postfix:
            x = self.postfix.popleft()
            if x in SmartCalculator.order_of_operators.keys():
                if not self.actions[x]():
                    return
            else:
                self.operation_stack.append(x)
        value = self.get_value(self.operation_stack[0])
        if value is not None:
            self.result = value

    @get_operands
    def divide(self, operand_1, operand_2):
        self.operation_stack.append(operand_1 / operand_2)

    def get_value(self, operand):
        sign = 1
        if SmartCalculator.is_correct_variable(operand):
            if operand[0] == '-':
                sign = -1
                operand = operand[1:]
            result = self.variables.get(operand, None)
            if result is None:
                self.result = 'Unknown variable'
            else:
                result *= sign
        else:
            try:
                result = sign * int(operand)
            except ValueError:
                self.result = 'Invalid identifier'
                result = None
        return result

    def handle(self, input_str):
        if input_str == '/help':
            self.print_help()
        elif len(input_str.strip()) and input_str.strip()[0] == '/':
            print('Unknown command')
        else:
            if self.parse(input_str):
                self.calculate()
            if self.need_to_print:
                print(self.result)

    @staticmethod
    def is_correct_variable(x):
        if isinstance(x, str):
            return x.isalpha()
        return False

    @staticmethod
    def is_unary_operator(operator, prev_operator):
        return operator in '+-' and prev_operator in (None, *'+-*/=(')

    @get_operands
    def multiply(self, operand_1, operand_2):
        self.operation_stack.append(operand_1 * operand_2)

    def parse(self, input_expression):
        if input_expression:
            for operator in SmartCalculator.order_of_operators.keys():
                input_expression = input_expression.replace(operator, f' {operator} ')
            expression = deque()
            operators = []
            brackets = []
            for x in input_expression.split():
                if x in '+-*/=':
                    operators.append(x)
                else:
                    if operators:
                        if any(operators.count(operator) > 1 for operator in '*/')\
                                or all(bool(operators.count(operator)) for operator in '*/')\
                                or (len(operators) > 1 and operators[-1] in '*/')\
                                or operators.count('=') > 1\
                                or (not all(operators[0] == operator for operator in operators[:-1])):
                            self.result = 'Invalid expression'
                            return False

                        if len(operators) > 1:
                            if any(operator in operators for operator in '*/'):
                                expression.extend(operators)
                            elif operators[0] == operators[-1]:
                                if operators[0] == '+':
                                    expression.append('+')
                                else:
                                    expression.append('-' if operators.count('-') % 2 else '+')
                            else:
                                if operators[0] == '+':
                                    expression.append('-')
                                else:
                                    expression.append('+' if operators.count('-') % 2 else '-')
                        else:
                            expression.append(operators[0])
                        operators.clear()

                    if x == '(':
                        brackets.append('(')
                    if x == ')':
                        try:
                            brackets.pop()
                        except IndexError:
                            self.result = 'Invalid expression'
                            return False
                    expression.append(x)
            if brackets:
                self.result = 'Invalid expression'
                return False
            return self.parse_infix_to_postfix(expression)
        self.need_to_print = False
        return False

    def parse_infix_to_postfix(self, input_expression):
        if input_expression:
            self.postfix.clear()
            operators = []
            prev_x = None
            while input_expression:
                x = input_expression.popleft()
                if SmartCalculator.is_unary_operator(x, prev_x):
                    unary_operator = x
                    x = input_expression.popleft()
                else:
                    unary_operator = ''
                if x not in SmartCalculator.order_of_operators.keys():
                    self.postfix.append(unary_operator + x)
                else:
                    if not operators or operators[-1] in '(=':
                        operators.append(x)
                    elif x == ')':
                        while operators[-1] != '(':
                            self.postfix.append(operators.pop())
                        operators.pop()  # remove '('
                    else:
                        prev_operator = operators[-1]
                        while SmartCalculator.order_of_operators[x] <= SmartCalculator.order_of_operators[prev_operator]:
                            self.postfix.append(operators.pop())
                            if not operators or operators[-1] in '(=':
                                break
                            prev_operator = operators[-1]
                        operators.append(x)
                prev_x = x
            while operators:
                self.postfix.append(operators.pop())
            return True
        self.need_to_print = False
        return False

    @get_operands
    def pow(self, operand_1, operand_2):
        self.operation_stack.append(operand_1 ** operand_2)

    @staticmethod
    def print_help():
        print('The program calculates the sum, subtraction, multiplication, integer division, power of numbers\n'
              'The program supports variables, parentheses.\n'
              'Rules for variables:\n'
              '\t- Name of a variable (identifier) can contain only Latin letters;\n'
              '\t- A variable can have a name consisting of more than one letter;\n'
              '\t- The case is also important; for example, n is not the same as N;\n'
              '\t- The value can be an integer number or a value of another variable;\n'
              '\t- It is possible to set a new value to an existing variable;\n'
              '\t- To print the value of a variable you should just type its name;\n\n'
              'Example (the greater-than symbol followed by space (>) represents the user input):\n'
              '> -2 + 4 - 5 + 6\n'
              '3\n'
              '> 9 +++ 10 -- 8\n'
              '27\n'
              '> 3 --- 5\n'
              '-2\n'
              '> 14       -   12\n'
              '2\n'
              '> a  =  3\n'
              '> b= 4\n'
              '> c =5\n'
              '> d = a + b - c\n'
              '> d\n'
              '2\n'
              '> 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)\n'
              '121\n'
              '> 2*2^3\n'
              '16\n')

    @get_operands
    def subtract(self, operand_1, operand_2):
        self.operation_stack.append(operand_1 - operand_2)


if __name__ == '__main__':
    main()

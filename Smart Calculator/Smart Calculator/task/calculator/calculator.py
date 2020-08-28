def main():
    smart_calculator = SmartCalculator()
    answer = input().strip()
    while answer != '/exit':
        smart_calculator.handle(answer)
        answer = input().strip()
    print('Bye!')


class SmartCalculator:
    available_operations = ('-', '+')
    available_commands = ('/help',)

    def __init__(self):
        self.result = 0
        self.input = []

    def add(self, number):
        self.result += number

    def calculate(self):
        self.result = 0
        for x in self.input:
            self.add(x)

    def handle(self, input_str):
        if input_str == '/help':
            self.print_help()
        else:
            if self.parse_input(input_str):
                self.calculate()
                print(self.result)

    def parse_input(self, input_str):
        if input_str:
            self.input.clear()
            sign = 1
            for x in input_str.strip().split():
                try:
                    self.input.append(sign * int(x))
                except ValueError:
                    if x[0] == '/' and len(x) > 1:
                        print('Unknown command')
                        return False
                    if not all(x[0] == x[i] for i in range(len(x))):
                        print('Invalid expression')
                        return False
                    if x[0] not in SmartCalculator.available_operations:
                        print('Invalid expression')
                        return False
                    sign = -1 if x.count('-') % 2 else 1
            return True
        return False

    @staticmethod
    def print_help():
        print('The program calculates the sum and subtraction of numbers\n'
              'Example:\n'
              '-2 + 4 - 5 + 6 equals 3\n'
              '9 +++ 10 -- 8 equals 27\n'
              '3 --- 5 equals -2\n'
              '14       -   12 equals 2\n')


if __name__ == '__main__':
    main()

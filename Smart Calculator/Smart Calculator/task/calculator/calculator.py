from collections import deque


class SmartCalculator:
    def __init__(self):
        self.result = 0
        self.input = None

    def calculate(self):
        self.result = 0
        sign = 1
        for x in self.input:
            if SmartCalculator.is_number(x):
                self.add(sign * int(x))
            else:
                sign = -1 if x.count('-') % 2 else 1

    @staticmethod
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def handle(self, input_str):
        if input_str == '/help':
            self.print_help()
        else:
            if input_str:
                self.input = input_str.strip().split()
                self.calculate()
                print(self.result)

    @staticmethod
    def print_help():
        print('The program calculates the sum and subtraction of numbers\n'
              'Example:\n'
              '-2 + 4 - 5 + 6 equals 3\n'
              '9 +++ 10 -- 8 equals 27\n'
              '3 --- 5 equals -2\n'
              '14       -   12 equals 2\n')

    def add(self, number):
        self.result += number


def main():
    smart_calculator = SmartCalculator()
    answer = input().strip()
    while answer != '/exit':
        smart_calculator.handle(answer)
        answer = input().strip()
    print('Bye!')


if __name__ == '__main__':
    main()

class SmartCalculator:
    def __init__(self):
        self.input = None

    def sum(self):
        return sum(int(x) for x in self.input.split())

    @staticmethod
    def print_help():
        print('The program calculates the sum of numbers')

    def handle(self, input_str):
        self.input = input_str.strip()
        if self.input == '/help':
            self.print_help()
        else:
            if self.input:
                print(self.sum())


def main():
    smart_calculator = SmartCalculator()
    answer = input().strip()
    while answer != '/exit':
        smart_calculator.handle(answer)
        answer = input().strip()
    print('Bye!')


if __name__ == '__main__':
    main()

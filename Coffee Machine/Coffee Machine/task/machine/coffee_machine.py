class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.next_step = 'main_menu'
        self.fill_position = -1

    def __str__(self):
        return f'''
        The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.disposable_cups} of disposable cups
        ${self.money} of money'''

    def show_main_menu(self):
        print('\nWrite action (buy, fill, take, remaining, exit):')
        self.next_step = 'execute'

    def show_buy_menu(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        self.next_step = 'buy_handle'

    def show_fill_menu(self):
        products = [['ml', 'water'],
                    ['ml', 'milk'],
                    ['grams', 'coffee beans'],
                    ['disposable cups', 'coffee']]
        self.fill_position += 1
        print(f'Write how many {products[self.fill_position][0]} of {products[self.fill_position][1]} do you want '
              f'to add:')
        self.next_step = 'fill_handle'

    def find_missing_resources(self, water, milk, coffee_beans, disposable_cups):
        missing_resources = []
        if self.water < water:
            missing_resources.append('water')
        if self.milk < milk:
            missing_resources.append('milk')
        if self.coffee_beans < coffee_beans:
            missing_resources.append('coffee_beans')
        if self.disposable_cups < disposable_cups:
            missing_resources.append('disposable_cups')
        return missing_resources

    def reduce_resources(self, water, milk, coffee_beans, disposable_cups):
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.disposable_cups -= disposable_cups

    def buy(self, coffee_type):

        if coffee_type == 'back':
            self.show_main_menu()
            return

        water = milk = coffee_beans = disposable_cups = money = 0
        if coffee_type == '1':
            water = 250
            coffee_beans = 16
            disposable_cups = 1
            money = 4
        elif coffee_type == '2':
            water = 350
            milk = 75
            coffee_beans = 20
            disposable_cups = 1
            money = 7
        elif coffee_type == '3':
            water = 200
            milk = 100
            coffee_beans = 12
            disposable_cups = 1
            money = 6
        else:
            print('You made mistake. Try again\n')
            self.show_buy_menu()
            return

        missing_resources = self.find_missing_resources(water, milk, coffee_beans, disposable_cups)
        if len(missing_resources) == 0:
            print('I have enough resources, making you a coffee!')
            self.reduce_resources(water, milk, coffee_beans, disposable_cups)
            self.money += money
        else:
            print('Sorry, not enough', ', '.join(missing_resources) + '!')
        self.show_main_menu()

    def fill(self, number):
        if self.fill_position == 0:
            self.water += number
            self.show_fill_menu()
        elif self.fill_position == 1:
            self.milk += number
            self.show_fill_menu()
        elif self.fill_position == 2:
            self.coffee_beans += number
            self.show_fill_menu()
        elif self.fill_position == 3:
            self.disposable_cups += number
            self.fill_position = -1
            self.show_main_menu()

    def take(self):
        print('I gave you $', self.money)
        self.money = 0

    def handle(self, input_value=''):
        if self.next_step == 'main_menu':
            self.show_main_menu()
        elif self.next_step == 'buy':
            self.show_buy_menu()
        elif self.next_step == 'buy_handle':
            self.buy(input_value)
        elif self.next_step == 'fill':
            self.show_fill_menu()
        elif self.next_step == 'fill_handle':
            self.fill(int(input_value))
        elif self.next_step == 'take':
            self.take()
            self.show_main_menu()
        elif self.next_step == 'remaining':
            print(self)
            self.show_main_menu()
        elif self.next_step == 'execute':
            self.next_step = input_value
            self.handle('')
        else:
            print('Unknown command. Try again.')
            self.show_main_menu()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
action = ''
while not action == 'exit':
    coffee_machine.handle(action)
    action = input()

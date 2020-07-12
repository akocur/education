import random


class CreditCard:
    BIN = 400000
    credit_cards = {}  # {card_number: self}
    current_account_identifier = 844943345

    def __init__(self):
        self.account_identifier = CreditCard.current_account_identifier + 1
        self.pin = random.randint(1000, 9999)
        self.checksum = self.get_checksum()
        self.balance = 0
        CreditCard.current_account_identifier += 1
        CreditCard.credit_cards[self.get_card_number()] = self

    def __str__(self):
        return f'''Your card number:
{self.get_card_number()}
Your card PIN:
{self.pin}'''

    @staticmethod
    def exist(number, pin):
        card = CreditCard.credit_cards.get(number)
        if card is None:
            return False
        return str(card.pin) == pin

    def get_card_number(self):
        return str(self.BIN) + str(self.account_identifier).rjust(9, '0') + str(self.checksum)

    def get_checksum(self):
        number = str(self.BIN) + str(self.account_identifier).rjust(9, '0')
        digits = []
        for i in range(len(number)):
            x = int(number[i])
            if i % 2:
                digits.append(x)  # because i begin with 0
            else:
                if 2 * x > 9:
                    digits.append(2 * x - 9)
                else:
                    digits.append((2 * x))
        return (10 - sum(digits) % 10) % 10

    @staticmethod
    def get_credit_card(number):
        return CreditCard.credit_cards.get(number)


class Menu:
    def __init__(self):
        main_menu = {'1': ['1. Create an account', self.create_account],
                     '2': ['2. Log into account', self.log_into_account],
                     '0': ['0. Exit', self.exit],
                     }

        log_into_account_menu = {'1': ['1. Balance', self.balance],
                                 '2': ['2. Log out', self.log_out],
                                 '0': ['0. Exit', self.exit],
                                 }

        self.menu = [main_menu, log_into_account_menu]
        self.current_menu = self.menu[0]
        self.account = None

    def balance(self):
        print(f'\nBalance {self.account.balance}')
        self.shows_menu()

    def create_account(self):
        credit_card = CreditCard()
        print('\nYour card has been created', credit_card, sep='\n')
        self.shows_menu()

    def handle(self, answer):
        function = self.current_menu[answer][1]
        return function()

    def log_into_account(self):
        print('Enter your card number:')
        number = input()
        print('Enter your PIN:')
        pin = input()
        if CreditCard.exist(number, pin):
            print('\nYou have successfully logged in!')
            self.account = CreditCard.get_credit_card(number)
            self.current_menu = self.menu[1]
        else:
            print('\nWrong card number or PIN!')
        self.shows_menu()

    def log_out(self):
        print('\nYou have successfully logged out!')
        self.current_menu = self.menu[0]
        self.shows_menu()

    def shows_menu(self):
        print('', *list(option[0] for option in self.current_menu.values()), sep='\n')

    @staticmethod
    def exit():
        print('\nBye!')
        return True


menu = Menu()
menu.shows_menu()
while not menu.handle(input().strip()):
    pass

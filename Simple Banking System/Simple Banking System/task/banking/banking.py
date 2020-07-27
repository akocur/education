import random
import sqlite3


class CreditCard:
    BIN = 400000

    def __init__(self, sqlite3_connect=sqlite3.connect(':memory:'), number=None, pin=None, balance=0):
        self.sqlite3_connect = sqlite3_connect
        self.number = CreditCard.get_last_number(sqlite3_connect) + 1 if number is None else number
        self.pin = random.randint(1000, 9999) if pin is None else pin
        self.checksum = self.get_checksum()
        self.balance = balance

    def __str__(self):
        return f'''Your card number:
{self.get_card_number()}
Your card PIN:
{self.pin}'''

    @staticmethod
    def is_exist(sqlite3_connect, number, pin):
        cursor = sqlite3_connect.cursor()
        cursor.execute('''
            SELECT
                id
            FROM 
                card
            WHERE
                number = ? AND pin = ?
            ''', (number, pin))
        sqlite3_connect.commit()
        row = cursor.fetchone()
        cursor.close()
        return False if row is None else True

    def get_card_number(self):
        return str(self.BIN) + str(self.number).rjust(9, '0') + str(self.checksum)

    def get_checksum(self):
        number = str(self.BIN) + str(self.number).rjust(9, '0')
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
    def get_credit_card(sqlite3_connect, number):
        cursor = sqlite3_connect.cursor()
        cursor.execute('''
            SELECT
                number,
                pin,
                balance
            FROM
                card
            WHERE
                number = ?
            ''', (number,))
        sqlite3_connect.commit()
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return CreditCard(sqlite3_connect, int(str(row[0])[len(str(CreditCard.BIN)):-1]), int(row[1]), row[2])

    @staticmethod
    def get_last_number(sqlite3_connect):
        cursor = sqlite3_connect.cursor()
        cursor.execute('''
            SELECT
                number
            FROM
                card
            ORDER BY number DESC
            ''')
        sqlite3_connect.commit()
        row = cursor.fetchone()
        cursor.close()
        return -1 if row is None else int(str(row[0])[len(str(CreditCard.BIN)):-1])

    def saves_in_database(self):
        cursor = self.sqlite3_connect.cursor()
        cursor.execute('''
            SELECT
                id
            FROM
                card
            WHERE
                number = ?
            ''', (int(self.get_card_number()),))
        row = cursor.fetchone()
        if row is None:
            cursor.execute('''
                INSERT INTO card (number, pin, balance)
                VALUES(?, ?, ?)''', (self.get_card_number(), self.pin, self.balance))
        else:
            cursor.execute('''
                UPDATE card
                SET                 
                    pin = ?,
                    balance = ?
                WHERE
                    number = ?
                ''', (self.pin, self.balance, self.get_card_number()))
        self.sqlite3_connect.commit()
        cursor.close()


class Menu:
    def __init__(self, sqlite3_connect=sqlite3.connect(':memory:')):
        main_menu = {'1': ['1. Create an account', self.create_account],
                     '2': ['2. Log into account', self.log_into_account],
                     '0': ['0. Exit', None],
                     }

        log_into_account_menu = {'1': ['1. Balance', self.balance],
                                 '2': ['2. Log out', self.log_out],
                                 '0': ['0. Exit', None],
                                 }

        self.menu = [main_menu, log_into_account_menu]
        self.current_menu = self.menu[0]
        self.account = None
        self.sqlite3_connect = sqlite3_connect

    def balance(self):
        print(f'\nBalance: {self.account.balance}')

    def create_account(self):
        credit_card = CreditCard(self.sqlite3_connect)
        credit_card.saves_in_database()
        print('\nYour card has been created', credit_card, sep='\n')

    def log_into_account(self):
        print('Enter your card number:')
        number = input()
        print('Enter your PIN:')
        pin = input()
        if CreditCard.is_exist(self.sqlite3_connect, number, pin):
            print('\nYou have successfully logged in!')
            self.account = CreditCard.get_credit_card(self.sqlite3_connect, number)
            self.current_menu = self.menu[1]
        else:
            print('\nWrong card number or PIN!')

    def log_out(self):
        print('\nYou have successfully logged out!')
        self.current_menu = self.menu[0]

    def shows(self):
        print('', *list(option[0] for option in self.current_menu.values()), sep='\n')
        answer = input().strip()
        while not answer == '0':
            function = self.current_menu[answer][1]
            function()
            print('', *list(option[0] for option in self.current_menu.values()), sep='\n')
            answer = input().strip()
        print('\nBye!')


connect = sqlite3.connect('card.s3db')
cur = connect.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance INTEGER DEFAULT 0
)
''')
connect.commit()
cur.close()
menu = Menu(connect)
menu.shows()
connect.close()

from math import log, ceil, floor
import argparse


class CreditCalculator:
    def __init__(self, type_calc='annuity', payment=0, periods=0, interest=0, principal=0):
        self.type = type_calc
        self.payment = payment
        self.periods = periods
        self.interest = interest
        self.principal = principal
        self.interest_rate = self.interest / 1200
        self.total_payments = 0

    def __repr__(self):
        return f'''
            type: {self.type}
            payment: {self.payment}
            periods: {self.periods}
            interest: {self.interest}
            principal: {self.principal}
            interest_rate: {self.interest_rate}
            total_payments: {self.total_payments}
            '''

    def overpayment(self):
        print(f'\nOverpayment = {self.total_payments - self.principal}')

    def are_errors(self):
        if self.type not in ['annuity', 'diff']:
            return True
        if self.interest <= 0 or self.payment < 0 or self.periods < 0 or self.principal < 0:
            return True
        if self.type == 'annuity':
            if self.payment == self.periods == self.principal == 0:
                return True
        else:
            if self.payment:
                return True

    def calculate(self):
        if self.are_errors():
            print('Incorrect parameters')
            return

        if self.type == 'annuity':
            if self.principal == 0:
                self.principal = floor(self.payment * (pow(1 + self.interest_rate, self.periods) - 1) /
                                       (self.interest_rate * pow(1 + self.interest_rate, self.periods)))
                print(f'Your credit principal = {self.principal}!')
            elif self.payment == 0:
                self.payment = ceil(self.principal * self.interest_rate * pow(1 + self.interest_rate, self.periods) /
                                    (pow(1 + self.interest_rate, self.periods) - 1))
                print(f'Your annuity payment = {self.payment}!')
            elif self.periods == 0:
                self.periods = ceil(log(self.payment / (self.payment - self.interest_rate * self.principal),
                                        1 + self.interest_rate))
                n_years = self.periods // 12
                n_month = self.periods % 12
                n_years_str = '' if n_years < 1 else f'{n_years} year{"s" if n_years > 1 else ""}'
                and_str = ' and ' if n_years > 0 and n_month > 0 else ''
                n_month_str = '' if n_month < 1 else f'{n_month} month{"s" if n_month > 1 else ""}'
                print(f'You need {n_years_str}{and_str}{n_month_str} to repay this credit!')
            self.total_payments = self.payment * self.periods
        elif self.type == 'diff':
            sum_payment = 0
            for month in range(1, self.periods + 1):
                payment = ceil(self.principal / self.periods + self.interest_rate * (self.principal - self.principal *
                                                                                     (month - 1) / self.periods))
                print(f'Month {month}: paid out {payment}')
                sum_payment += payment
            self.total_payments = sum_payment
        self.overpayment()


parser_args = argparse.ArgumentParser()
parser_args.add_argument('--type')
parser_args.add_argument('--payment', type=int, default=0)
parser_args.add_argument('--principal', type=int, default=0)
parser_args.add_argument('--periods', type=int, default=0)
parser_args.add_argument('--interest', type=float, default=0)
args = parser_args.parse_args()

credit_calc = CreditCalculator(args.type, args.payment, args.periods, args.interest, args.principal)
credit_calc.calculate()

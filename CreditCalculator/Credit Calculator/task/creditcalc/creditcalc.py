from math import log, ceil, floor


def input_remaining_values():
    global answer, credit_principal, monthly_payment, n_month, credit_interest

    if answer not in ['n', 'a', 'p']:
        print('Error. Unknown command.')
        return
    if not answer == 'p':
        print('Enter credit principal:')
        credit_principal = int(input('> '))
    if not answer == 'a':
        print('Enter monthly payment:')
        monthly_payment = float(input())
    if not answer == 'n':
        print('Enter count of periods:')
        n_month = int(input())
    print('Enter credit interest:')
    credit_interest = float(input())


def output_result():
    global answer, credit_principal, monthly_payment, n_month, credit_interest

    i = credit_interest / 1200
    if answer == 'p':
        credit_principal = floor(monthly_payment * (pow(1 + i, n_month) - 1) / (i * pow(1 + i, n_month)))
        print(f'Your credit principal = {credit_principal}!')
    elif answer == 'a':
        monthly_payment = ceil(credit_principal * i * pow(1 + i, n_month) / (pow(1 + i, n_month) - 1))
        print(f'Your annuity payment = {monthly_payment}!')
    elif answer == 'n':
        n_month = ceil(log(monthly_payment / (monthly_payment - i * credit_principal), 1 + i))
        n_years = n_month // 12
        n_month %= 12
        n_years_str = '' if n_years < 1 else f'{n_years} year{"s" if n_years > 1 else ""}'
        and_str = ' and ' if n_years > 0 and n_month > 0 else ''
        n_month_str = '' if n_month < 1 else f'{n_month} month{"s" if n_month > 1 else ""}'
        print(f'You need {n_years_str}{and_str}{n_month_str} to repay this credit!')


credit_principal = monthly_payment = n_month = credit_interest = 0
print('What do you want to calculate?',
      'type "n" - for count of months',
      'type "a" - for annuity monthly payment',
      'type "p" - for monthly payment',
      sep='\n')
answer = input('> ')
input_remaining_values()
output_result()

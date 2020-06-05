print('Enter the credit principal')
credit_principal = int(input('> '))
print('What do you want to calculate?',
      'type "m" - for count of months',
      'type "p" - for monthly payment',
      sep='\n')
answer = input()
if answer == 'm':
    print('Enter monthly payment:')
    monthly_payment = int(input())
    n_month = credit_principal // monthly_payment
    if credit_principal % monthly_payment:
        n_month += 1
    print('\nIt take {} month{} to repay the credit'.format(n_month, 's' if n_month > 1 else ''))
elif answer == 'p':
    print('Enter count of months:')
    n_month = int(input())
    monthly_payment = credit_principal // n_month
    if credit_principal % n_month:
        monthly_payment += 1
    last_month_payment = credit_principal - (n_month - 1) * monthly_payment
    addition = '' if last_month_payment == monthly_payment else f' with last month payment = {last_month_payment}'
    print(f'Your monthly payment = {monthly_payment}{addition}')
else:
    print('Error. Unknown command.')

# put your python code here
first_number = float(input().strip())
second_number = float(input().strip())
operator = input().strip()

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '/':
    print('Division by 0!' if second_number == 0 else first_number / second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == 'mod':
    print('Division by 0!' if second_number == 0 else first_number % second_number)
elif operator == 'pow':
    print(first_number ** second_number)
elif operator == 'div':
    print('Division by 0!' if second_number == 0 else first_number // second_number)
else:
    print("Unknown operator")

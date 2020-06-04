begin_amount_atoms = int(input())
requared_amount_atoms = int(input())

amount_days = 0
current_amount_atoms = begin_amount_atoms
while current_amount_atoms > requared_amount_atoms:
    amount_days += 12
    current_amount_atoms /= 2
print(amount_days)

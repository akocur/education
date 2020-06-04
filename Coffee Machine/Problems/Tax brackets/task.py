def percent(income_):
    if income_ >= 132407:
        return 28
    if income_ >= 42708:
        return 25
    if income_ >= 15528:
        return 15

    return 0


income = int(input())
print(f'The tax for {income} is {percent(income)}%. That is {income * percent(income) / 100:.0f} dollars!')

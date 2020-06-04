sum_ = 0
amount = 0
number = input()
while not number == '.':
    sum_ += int(number)
    amount += 1
    number = input()
print('0' if amount == 0 else sum_ / amount)

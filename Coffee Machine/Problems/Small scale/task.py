number = input()
min_ = float('inf')
while not number == '.':
    if float(number) < min_:
        min_ = float(number)
    number = input()
print(min_)

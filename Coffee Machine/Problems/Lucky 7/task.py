n = int(input())

numbers = ''
for _i in range(n):
    number = int(input())
    if number % 7 == 0:
        numbers += str(number * number) + '\n'

print(numbers)

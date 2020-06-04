number = int(input())
for i in range(2, int(number ** 0.5 + 1)):
    if not number % i:
        print('This number is not prime')
        break
    i += 1
else:
    print('This number is not prime' if number == 1 else 'This number is prime')

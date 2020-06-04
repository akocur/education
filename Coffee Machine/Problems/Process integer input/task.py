# put your python code here
numbers = []
while True:
    number = int(input())
    if number > 100:
        break
    if number < 10:
        continue
    numbers.append(number)

for number in numbers:
    print(number)

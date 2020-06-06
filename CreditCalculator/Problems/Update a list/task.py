numbers = [4, 1, 0, 3, 2, 5]
index = 0
while index < len(numbers):
    numbers[index] = index
    index += 1
print(numbers)

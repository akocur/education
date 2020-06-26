height = int(input())
for i in range(1, height + 1):
    row = '#' * (2 * i - 1)
    print(row.center(2 * height - 1))

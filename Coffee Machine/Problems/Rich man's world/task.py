deposit = int(input())

years = 0
while 50000 <= deposit <= 700000:
    deposit *= 1.071
    years += 1
print(years)

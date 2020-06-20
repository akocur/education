digits = [int(x) for x in input()]
print([(digits[i] + digits[i + 1]) / 2 for i in range(len(digits) - 1)])

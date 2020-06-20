digits = [int(x) for x in input()]
print([sum(x for x in digits[:i + 1]) for i in range(len(digits))])

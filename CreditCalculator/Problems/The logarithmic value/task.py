from math import log


x = int(input())
base = int(input())
print(round(log(x, base) if base > 1 else log(x), 2))

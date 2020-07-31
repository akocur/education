# put your python code here
words = input().lower().split()
statistics = {}
for word in words:
    statistics[word] = statistics.get(word, 0) + 1
print(*[f'{key} {value}' for key, value in statistics.items()], sep='\n')

text = input().strip()

result = ''
for char in text:
    if char.islower():
        result += char
    else:
        result += '_' + char.lower()
print(result)

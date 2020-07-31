# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
items = list(test_dict.items())
items.sort(key=lambda row: row[1])
print(f'min: {items[0][0]}', f'max: {items[-1][0]}', sep='\n')

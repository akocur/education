numbers = input().split()
number = input()
found_indexes = [str(i) for i in range(len(numbers)) if numbers[i] == number]
print(' '.join(found_indexes) if len(found_indexes) > 0 else 'not found')

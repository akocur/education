dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input().split()
incorrect_words = [word for word in words if word not in dictionary]
print('OK' if len(incorrect_words) == 0 else '\n'.join(incorrect_words))

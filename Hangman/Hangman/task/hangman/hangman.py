import random


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
hint = word[:3] + '-' * (len(word) - 3)
answer = input(f'Guess the word: {hint}  > ')
print('You survived!' if word == answer else 'You are hanged!')

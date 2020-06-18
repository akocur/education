import random


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
answer = input('Guess the word: > ')
print('You survived!' if word == answer else 'You are hanged!')

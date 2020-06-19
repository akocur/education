import random


def shows_result():
    global word, input_correct_letters

    result = '\n'
    for letter in word:
        if letter in input_correct_letters:
            result += letter
        else:
            result += '-'
    print(result)


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
letters_of_word = set(word)
input_correct_letters = set()

for _i in range(8):
    shows_result()
    input_letter = input('Input a letter: > ')
    if input_letter in letters_of_word:
        input_correct_letters.add(input_letter)
    else:
        print('No such letter in the word')

print('\nThanks for playing!', "We'll see how well you did in the next stage", sep='\n')

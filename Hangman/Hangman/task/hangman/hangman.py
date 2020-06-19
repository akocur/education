import random


class Hangman:
    def __init__(self, words, lives):
        self.lives = lives
        self.words = words
        self.word = random.choice(words)
        self.letters_of_word = set(self.word)
        self.input_correct_letters = set()
        self.result = '-' * len(self.word)

    def set_result(self):
        result = ''
        for letter in self.word:
            if letter in self.input_correct_letters:
                result += letter
            else:
                result += '-'
        self.result = result

    def play(self):
        print('H A N G M A N')

        while self.lives > 0 and len(self.letters_of_word) > len(self.input_correct_letters):
            print('', self.result, sep='\n')
            input_letter = input('Input a letter: > ')
            if input_letter in self.letters_of_word:
                if input_letter in self.input_correct_letters:
                    print('No improvements')
                    self.lives -= 1
                else:
                    self.input_correct_letters.add(input_letter)
            else:
                print('No such letter in the word')
                self.lives -= 1
            self.set_result()

        if self.input_correct_letters == self.letters_of_word:
            print('', self.word, 'You guessed the word!', 'You survived!', sep='\n')
        else:
            print('You are hanged!')


game = Hangman(('python', 'java', 'kotlin', 'javascript'), 8)
game.play()

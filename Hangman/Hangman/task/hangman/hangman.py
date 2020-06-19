import random


class Hangman:
    def __init__(self, words, lives):
        self.original_lives = lives
        self.lives = lives
        self.words = words
        self.word = random.choice(words)
        self.letters_of_word = set(self.word)
        self.correct_letters = set()
        self.incorrect_letters = set()
        self.result = '-' * len(self.word)

    def __repr__(self):
        return f'''
    self.original_lives = {self.original_lives}
    self.lives = {self.lives}
    self.words = {self.words}
    self.word = {self.word}
    self.letters_of_word = {self.letters_of_word}
    self.correct_letters = {self.correct_letters}
    self.incorrect_letters = {self.incorrect_letters}
    self.result = {self.result}
        '''

    def set_result(self):
        result = ''
        for letter in self.word:
            if letter in self.correct_letters:
                result += letter
            else:
                result += '-'
        self.result = result

    def are_errors(self, input_letter):
        if not len(input_letter) == 1:
            print('You should input a single letter')
            return True
        if not input_letter.islower():
            print('It is not an ASCII lowercase letter')
            return True
        if input_letter in self.correct_letters or input_letter in self.incorrect_letters:
            print('You already typed this letter')
            return True
        return False

    def play(self):
        print('H A N G M A N')
        act = input('Type "play" to play the game, "exit" to quit: > ')
        while not act == 'exit':
            if not act == 'play':
                act = input('Type "play" to play the game, "exit" to quit: > ')
                continue

            self.__init__(self.words, self.original_lives)
            while self.lives > 0 and len(self.letters_of_word) > len(self.correct_letters):
                print('', self.result, sep='\n')
                input_letter = input('Input a letter: > ')

                if self.are_errors(input_letter):
                    continue

                if input_letter in self.letters_of_word:
                    self.correct_letters.add(input_letter)
                    self.set_result()
                else:
                    print('No such letter in the word')
                    self.incorrect_letters.add(input_letter)
                    self.lives -= 1

            if self.correct_letters == self.letters_of_word:
                print('', self.word, 'You guessed the word!', 'You survived!', sep='\n')
            else:
                print('You are hanged!')

            act = input('\nType "play" to play the game, "exit" to quit: > ')


game = Hangman(('python', 'java', 'kotlin', 'javascript'), 8)
game.play()

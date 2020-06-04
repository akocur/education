digits_in_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number = input()
for digit in number:
    print(digits_in_words[int(digit)])

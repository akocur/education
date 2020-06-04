text = input()
for char in text:
    if not char.isalpha():
        break
    print('vowel' if char.lower() in 'aeiou' else 'consonant')

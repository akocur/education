# put your python code here
text = input()
len_text = len(text)
if len_text % 2:
    print('Not palindrome')
else:
    index = 0
    while index < (len_text / 2):
        if text[index] != text[-(index + 1)]:
            print('Not palindrome')
            break
        index += 1
    else:
        print('Palindrome')

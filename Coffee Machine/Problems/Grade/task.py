score = int(input().strip())
maximum = int(input().strip())

percentage = 100 / maximum * score
if percentage >= 90:
    print('A')
elif percentage >= 80:
    print('B')
elif percentage >= 70:
    print('C')
elif percentage >= 60:
    print('D')
else:
    print('F')

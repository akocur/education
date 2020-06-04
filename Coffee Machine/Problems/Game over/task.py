scores = input().split()
# put your python code here
error = 0
correct_answer = 0
for answer in scores:
    if answer == 'I':
        error += 1
        if error == 3:
            print('Game over')
            print(correct_answer)
            break
        continue
    correct_answer += 1
else:
    print('You won')
    print(correct_answer)

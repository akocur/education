offset = int(input().strip())

if offset <= -11:
    print('Monday')
elif offset == 14:
    print('Wednesday')
else:
    print('Tuesday')

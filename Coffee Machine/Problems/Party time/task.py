guests = []
guest = input()
while not guest == '.':
    guests.append(guest)
    guest = input()
print(guests)
print(len(guests))

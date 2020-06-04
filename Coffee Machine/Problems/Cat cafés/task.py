string = input()
max_cats = 0
cafe_name = ''
while not string == 'MEOW':
    data = string.split()
    if int(data[1]) > max_cats:
        max_cats = int(data[1])
        cafe_name = data[0]
    string = input()
print(cafe_name)

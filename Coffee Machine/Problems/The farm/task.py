money = int(input())

chicken_count = money // 23
goat_count = money // 678
pig_count = money // 1296
cow_count = money // 3848
sheep_count = money // 6769

if sheep_count:
    print(sheep_count, 'sheep')
elif cow_count:
    print(cow_count, 'cows' if cow_count > 1 else 'cow')
elif pig_count:
    print(pig_count, 'pigs' if pig_count > 1 else 'pig')
elif goat_count:
    print(goat_count, 'goats' if goat_count > 1 else 'goat')
elif chicken_count:
    print(chicken_count, 'chickens' if chicken_count > 1 else 'chicken')
else:
    print('None')

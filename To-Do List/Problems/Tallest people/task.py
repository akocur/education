def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    tallest = [name for name in kwargs if kwargs[name] == max_height]
    for name in sorted(tallest):
        print(f'{name} : {max_height}')

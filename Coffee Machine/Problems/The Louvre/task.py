class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def get_info(self):
        print(f'"{self.title}" by {self.painter} ({self.year}) hangs in the {Painting.museum}.')


painting = Painting(input(), input(), input())
painting.get_info()

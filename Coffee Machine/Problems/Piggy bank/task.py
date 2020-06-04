class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, dollars, cents):
        self.cents += cents
        self.dollars += dollars + self.cents // 100
        self.cents = self.cents % 100

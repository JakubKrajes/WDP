from datetime import date


class Travel:

    goal: str
    price: float
    travel_date: date

    def __init__(self, cel: str, cena: float, data: date):
        self.goal = cel
        self.price = cena
        self.travel_date = data

    def __repr__(self):
        return f'cel = {self.goal}, cena = {self.price}, data = {self.travel_date}'

    def __lt__(self, other):
        if self.price == other.price:
            return self.travel_date < other.travel_date
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price and self.goal == other.goal


w = date.today()

y = date(2019, 3, 12)

z = Travel("cz", 1001, w)
x = Travel("w", 1001, y)

print(x>z)


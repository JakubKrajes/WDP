from lis import Travel
from datetime import date


class TrainJourney(Travel):

    train_class: int
    seat: str

    def __init__(self, cel: str, cena: float, data: date, klasa: int, siedzenie: str):
        self.train_class = klasa
        self.seat = siedzenie
        super(). __init__(cel, cena, data)

    def __repr__(self):
        return f'klasa = {self.train_class}, siedzenia = {self.seat}, cel = {self.goal}, cena = {self.price}, ' \
                f'=data = {self.travel_date}'


he = TrainJourney("WWA", 2000, date.today(), 3, "welurowe")

print(he)

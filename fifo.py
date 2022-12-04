from lis import Travel
from datetime import date
from aaaaaa import TrainJourney


class AirTravel(Travel):

    airline: str
    seat: str

    def __init__(self, cel: str, cena: float, data: date, linialotu: str, siedzenie: str):
        self.airline = linialotu
        self.seat  = siedzenie
        super().__init__(cel,cena,data)

    def __repr__(self):
        return f'linialotu = {self.airline}, siedzenia = {self.seat}, cel = {self.goal}, cena = {self.price}, ' \
                f'=data = {self.travel_date}'


x = Travel("WWA", 1001, date.today())
y = TrainJourney("SzCZ", 1002, date(2019, 11, 12), 3, "Najlepsze")
z = AirTravel("krak", 199, date(2018, 5, 12), "Ryanainr", "Wygodne")

lista = [x, y, z]

print(min(list))

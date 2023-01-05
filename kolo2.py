class Vechile:
    __reg: str
    __model: int
    __prod_year: int

    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022):
        if model < 0 and prod_year < 1900 or prod_year > 2022:
            self.__model = 0
            self.__prod_year = 2022
        self.__reg = reg
        self.__model = model
        self.__prod_year = prod_year

    def brake(self) -> str:
        return "Zatrzymuje się"

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.__prod_year}!'

    def __repr__(self):
        if self.__reg:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\nModel: {self.__model}\n'
        if self.__model:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\nRejestracja: {self.__reg}'
        if self.__prod_year:
            return f'Model: {self.__model}\nRejestracja: {self.__reg}'

    @property
    def reg(self) -> str:
        return self.__reg

    @property
    def model(self) -> int:
        return self.__model

    @property
    def prod_year(self) -> int:
        return self.__prod_year

    @reg.setter
    def reg(self, value: str) -> None:
        self.__reg = value

    @model.setter
    def model(self, value: int) -> None:
        if value < 0:
            print(f"Podano błędny model.{value} < 0 !")
        else:
            self.__model = value

    @prod_year.setter
    def prod_year(self, value: int) -> None:
        if value < 1900 or value > 2022:
            print(f"Podano błędny rok.{value} < 1900 lub {value} > 2022 !")
        else:
            self.__prod_year = value

    def __eq__(self, other):
        return self.__model == other.__model

    def __ne__(self, other):
        return self.__model != other.__model

from autko import Vechile


class Car(Vechile):

    __price: int
    __colour: str
    __extra_seats: int

    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022, price=0, colour=None, extra_seats=0):
        if price < 0:
            self.__price = 0
        self.__price = price
        if extra_seats < 0:
            self.__extra_seats = 0
        self.__extra_seats = extra_seats
        self.__colour = colour
        super().__init__(reg, model, prod_year)


    @property
    def price(self):
        return self.__price

    @property
    def colour(self):
        return self.__colour

    @property
    def extra_seats(self):
        return self.__extra_seats

    @price.setter
    def price(self, value: int):
        if value < 0:
            self.__price = 0
        self.__price = value

    @colour.setter
    def colour(self, value: str):
        self.__colour = value

    @extra_seats.setter
    def extra_seats(self, value: int):
        if value < 0:
            self.__extra_seats = 0
        self.__extra_seats = value

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.__prod_year}!, ma kolor {self.__colour}'

    def __eq__(self, other):
        return self.model == other.model and self.price == other.price

    def __ne__(self, other):
        return self.model != other.model and self.price != other.price

    def __repr__(self) -> str:

        if self.reg  and self.colour:
            return f'Pojazd wyprodukowany w roku:{self.prod_year}.\nModel:{self.model}.\nRejestracja:{self.reg}.\nCena:{self.price}.\nKolor:{self.colour}.\nDodatkowe siedzenia:{self.extra_seats}.'

        if self.reg:
            return f'Pojazd wyprodukowany w roku:{self.prod_year}.\nModel:{self.model}.\nRejestracja:{self.reg}.\nCena:{self.price}.\nDodatkowe siedzenia:{self.extra_seats}.'

        if self.colour:
            return f'Pojazd wyprodukowany w roku:{self.prod_year}.\nModel:{self.model}.\nCena:{self.price}.\nKolor:{self.colour}.\nDodatkowe siedzenia:{self.extra_seats}.'
        else:
            return f'Pojazd wyprodukowany w roku:{self.prod_year}.\nModel:{self.model}.\nCena:{self.price}.\nDodatkowe siedzenia:{self.extra_seats}.'

v1 = Car(None,12, 1123,12345,"czerwo",5)

print(v1)

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


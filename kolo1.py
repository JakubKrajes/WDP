import math
from math import pi

from typing import List


class Pizza:
    __price: float
    __toppings: List[str]
    __diameter: float

    def __init__(self, diameter: float, toppings: List[str] = []) -> None:
        if diameter < 20:
            print("Błędna średnica")
            exit(-10)
        else:
            self.__diameter = diameter
            self.__price = 0.005 * self.area(diameter) + len(toppings) * 2

        self.__toppings = toppings

    @staticmethod
    def area(diameter: float) -> float:
        return ((diameter / 2) * (diameter / 2)) * math.pi

    @property
    def diameter(self) -> float:
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: float) -> None:
        if diameter < 20:
            print("Błędna średnica")
            exit(-10)
        else:
            self.__diameter = diameter
            self.__price = 0.005 * self.area(diameter) + len(self.__toppings) * 2

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, toppings):
        self.__toppings = toppings

    def add_toppings(self, topping: str) -> None:
        self.__toppings.append(topping)
        self.__price = self.__price + 2

    def __repr__(self):
        if self.__toppings is not None:
            return f'Pizza: \n średnica: {self.__diameter} \n dodatki: {self.__toppings}\n' \
                   f'cena : {self.__price}'
        else:
            return f'Pizza: \n średnica: {self.__diameter} \n' \
                   f'cena : {self.__price}'

    def __add__(self, other) -> 'Pizza':
        if self.diameter > other.diameter:
            diam = self.__diameter
        else:
            diam = other.diameter

        top = self.__toppings + other.toppings

        return Pizza(diam, top)


p_1 = Pizza(30, ["ser", "szynka"])
p_2 = Pizza(35, ["ananas"])
print(p_1)
print(p_2)
from typing import List

from hehj import Pizza


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, how_many_slices: int, diameter: float, toppings: List[str]) -> None:
        if 4 <= how_many_slices <= 12 and how_many_slices % 2 == 0:
            self.__how_many_slices = how_many_slices
        else:
            print("błędna ilość kawałków")
            exit(-10)
        super().__init__(diameter, toppings)

    @property
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, how_many_slices: int) -> None:
        if 4 <= how_many_slices <= 12 and how_many_slices % 2 == 0:
            self.__how_many_slices = how_many_slices
        else:
            print("błędna ilość kawałków")
            exit(-10)

    def part_price(self, ordered_slices) -> None:

        self.price = self.price / ordered_slices

    def __repr__(self):
        if self.__toppings is not None:
            return f'Pizza: \n średnica: {self.__diameter} \n dodatki: {self.__toppings}\n' \
                   f'cena : {self.__price}\n kawałki: {self.__how_many_slices}\n ' \
                   f'cena za kawałek: {self.price / self.__how_many_slices} '

        else:
            return f'Pizza: \n średnica: {self.__diameter} \n' \
                   f'cena : {self.__price}\n kawałki: {self.__how_many_slices}\n ' \
                   f'cena za kawałek: {self.price / self.__how_many_slices} '



p_1= Pizza(30,["ser","szynka"])
p_2= Pizza(35,["ananas"])
print(p_1)
print(p_2)

p_1.diameter=35
p_1.add_toppings("czekolada")
print(p_1)

print(p_1 == p_2)

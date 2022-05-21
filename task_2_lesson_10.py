"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothe(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def calc_cloth(self):
        pass

class Coat(Clothe):
    def __init__(self, name: str, size: int) -> None:
        self.size = size
        super().__init__(name)

    @property
    def calc_cloth(self):
        return f'Площадь ткани для {self.name} {round(self.size / 6.5 + 0.5, 2)}'

class Suit(Clothe):
    def __init__(self, name: str, height: int) -> None:
        self.height = height
        super().__init__(name)

    @property
    def calc_cloth(self):
        return f'Площадь ткани для {self.name} {round(2 * self.height + 0.3, 2)}'

coat = Coat('пальто', 56)
suit = Suit('костюма', 45)
print(coat.calc_cloth)
print(suit.calc_cloth)

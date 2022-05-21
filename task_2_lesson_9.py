"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т
"""
class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calculat(self, mass: float, fatness: float) -> float:
        return self._length * self._width * mass * fatness

r = Road()
r._length = 20
r._width = 5000
print(r.calculat(mass = 25, fatness = 5))

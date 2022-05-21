"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
"""
class Cage(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка должна быть больше одной ячейки')
        self.size = size

    def __add__(self, other: 'Cage'):
        return Cage(self.size + other.size)

    def __sub__(self, other: 'Cage'):
        result = self.size - other.size
        if result > 0:
            return Cage(result)
        else:
            raise Exception(f'Ошибка!  {self} из {other} не может быть меньше 0!')

    def __mul__(self, other: 'Cage'):
        return Cage(self.size * other.size)

    def __truediv__(self, other: 'Cage'):
        return Cage(self.size // other.size)

    def make_order(self, row_size: int) -> str:
        r = ['*' * row_size for _ in range(self.size // row_size)]
        t = '*' * (self.size % row_size)
        r.append(t)
        return '\n'.join(r)

    def __str__(self):
        return '*' * self.size

if __name__ == '__main__':
    net_1 = Cage(2)
    net_2 = Cage(6)
    net_sum = net_1 + net_2
    try:
        net_m = net_1 - net_2
    except Exception as e:
        net_m = None
        print(e)
    net_m2 = net_2 - net_1
    net_mul = net_1 * net_2
    net_div = net_2 / net_1
    net_3 = Cage(18)
    order_18_5 = net_3.make_order(5)
    print('net_1\t', net_1)
    print('net_2\t', net_2)
    print('net\t\t', net_sum)
    print('net1\t', net_m)
    print('sub2\t', net_m2)
    print('mul\t\t', net_mul)
    print('div\t\t', net_div)
    print(f'\norder_18_5\n{order_18_5}')

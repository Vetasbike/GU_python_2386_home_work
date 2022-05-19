"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title: str
    def draw(self):
        print(f'"Запуск отрисовки"')


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "ручкой"

    def draw(self):
        super().draw()
        print(f'"Пишем {self.title}"')
        return None



class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "карандашом"

    def draw(self):
        super().draw()
        print(f'"Чертим {self.title}"')
        return None


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "маркером"
    def draw(self):
        super().draw()
        print(f'"Выделяем {self.title}"')
        return None


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()

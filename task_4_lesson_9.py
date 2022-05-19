"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""
class Car:

    def __init__(self, name, speed, color, is_police = False) -> None:
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехала.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превышаете скорость на {self.speed - 60}.'
        else:
            return f'Ваша скорость нормальная {self.name}.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превышаете скорость на {self.speed - 40}.'
        else:
            return f'Ваша скорость нормальная {self.name}.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)


town = TownCar('Смарт', 80, 'белый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('на право'), town.turn('на лево'), town.stop())

sport = SportCar('Феррари', 250, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('на право'), sport.stop())

work = WorkCar('Приора', 30, 'черный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('на право'), work.stop())

police = PoliceCar('Мерседес', 100, 'голубой', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('на лево'), work.stop())
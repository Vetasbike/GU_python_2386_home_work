"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так
"""
from functools import wraps

def val_checker(in_value):

    def checker(val):

        @wraps(val)
        def decorate(x):
            if in_value(x):
                return val(x)
            raise ValueError from ValueError

        return decorate

    return checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)

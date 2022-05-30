"""
Написать декоратор для логирования типов позиционных аргументов функции
"""
from functools import wraps

def type_logger(level=0):

    def logger(aray):

        @wraps(aray)
        def resul(*argv):
            if level > 0:
                return 'calc_cube(' + ", ".join([f"{aray(x)}:{type(aray(x))}" for x in argv]) + ")"
            else:
                return "calc_cube(" + ", ".join([str(aray(x)) for x in argv]) + ")"
        return resul
    return logger

@ type_logger(2)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)

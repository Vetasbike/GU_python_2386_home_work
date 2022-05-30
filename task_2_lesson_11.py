"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""
class MyException(Exception):

    def div_func(self, a: int, b: int):
        try:
            result = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} - на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {result} \n")


m_e = MyException()

m_e.div_func(6, 7)
m_e.div_func(7, 0)
m_e.div_func(-5, 1)
m_e.div_func(0, 9)
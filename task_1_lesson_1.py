"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

def naive_realisation(duration: int):
    """

    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    # YOUR CODE HERE
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // 3600 % 24
    day = duration // 86400

    if duration < 60:
        total_time = f' до минуты: {duration} сек;'
    elif 60 <= duration < 3600:
        total_time = f' до часа: {minutes} мин {seconds} сек;'
    elif 3600 <= duration < 86400:
        total_time = f' до суток: {hours} час {minutes} мин {seconds} сек;'
    else:
        total_time = f' в остальных случаях: {day} дн {hours} час {minutes} мин {seconds} сек.'
    return total_time

if __name__ == '__main__':
    duration = 628
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))

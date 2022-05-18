'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
  этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.)
'''

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    hb = []
    for numder_i in dataset:
        numder_b = sum(map(int, str(numder_i)))
        if (numder_b % 7) == 0:
            hb.append(numder_i)
    return sum(hb)  # Верните значение полученной суммы

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    hbb = []
    for numder_i in dataset:
        numder_b = sum(map(int, str(numder_i + 17)))
        if (numder_b % 7) == 0:
            hbb.append(numder_i)
    return sum(hbb)  # Верните значение полученной суммы

if __name__ == '__main__':
    my_list = []
    for numder in range(1, 1000):
        if (numder % 2) != 0:
            numder = numder ** 3
            my_list.append(numder)

    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)

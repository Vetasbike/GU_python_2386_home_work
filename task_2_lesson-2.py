"""
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
"""
def off_plus(plus):
    if plus[0] in '+-':
        return plus[0]

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

val = 0
while val < len(my_list):
    change = off_plus(my_list[val])
    if my_list[val].isdigit() or (change and my_list[val][1:].isdigit()):
        if change:
            my_list[val] = change + my_list[val][1:].zfill(2)
        else:
            my_list[val] = my_list[val].zfill(2)

        my_list.insert(val, '"')
        my_list.insert(val + 2, '"')
        val += 2

    val += 1

print(my_list)
print(*my_list)
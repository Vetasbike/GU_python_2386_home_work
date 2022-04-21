"""
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
с сохранением порядка их следования в исходном списке, например:
"""
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [23, 1, 3, 10, 4, 11]

def search_for_items(argum):
    result = []
    for num in argum:
        if argum.count(num) == 1:
            result.append(num)
    return result


print([num for num in src if src.count(num) == 1])

print(search_for_items(src))


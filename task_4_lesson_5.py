"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def my_filter(num):
    for i in range(1, len(num)):
        if num[i] > num[i-1]:
            yield num[i]

def my_filter_shugar(num):
    return (num[i] for i in range(1, len(num)) if num[i] > num[i-1])


print(*my_filter(src))

print(*my_filter_shugar(src))
print(type(my_filter_shugar(src)))


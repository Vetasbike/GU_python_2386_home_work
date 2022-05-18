"""
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
генератор даст эффект.
"""
tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б',
    ]

def get_spisok(list1, list2):
    len_klasses = len(list2)
    for x, name in enumerate(list1):

        if x < len_klasses:
            yield (name, list2[x])
        else:
            yield (name, None)

print(type(get_spisok(tutors, klasses)))
print(*get_spisok(tutors, klasses))

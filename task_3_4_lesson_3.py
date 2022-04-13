"""

Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например: >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
"""

def thesaurus(*args):
    dictionary = {}

    for name in args:
        key_capital = name[0]
        if key_capital in dictionary.keys():
            dictionary[key_capital].append(name)
        else:
            dict_1 = [name]
            dictionary[key_capital] = dict_1
    return dictionary

def thesaurus_adv(*args):
    dictionary = {}

    for names in args:
        name, second_name = names.split()
        if not dictionary.get(second_name[0]):
            dictionary[second_name[0]] = {name[0]: [names]}
        elif not dictionary[second_name[0]].get(name[0]):
            (dictionary[second_name[0]])[name[0]] = [names]
        else:
            (dictionary[second_name[0]])[name[0]].append(names)

    return dictionary

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

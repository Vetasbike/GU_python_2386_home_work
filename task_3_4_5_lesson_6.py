"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
"""

import json
import os
import sys


def my_zip_gen(a_iter, b_iter):

    len_b = len(b_iter)

    return ((a_elem, b_iter[i]) if i < len_b else (a_elem, None)
            for i, a_elem in enumerate(a_iter))


def groping(
        output_file="./hobby_dictionary.txt",
        user_file="./users.csv",
        hobby_file="./hobby.csv"):

    if not (user_file or hobby_file):
        return sys.exit(-1)

    user_lines = None
    hobby_lines = None

    with open(user_file, "r", encoding="utf-8") as u_f:
        user_lines = u_f.readlines()

    with open(hobby_file, "r", encoding="utf-8") as h_f:
        hobby_lines = h_f.readlines()

    if len(user_lines) < len(hobby_lines):
        return sys.exit(1)

    together = {}

    for names, hobby in my_zip_gen(user_lines, hobby_lines):
        names = names.replace("\n", "").replace(",", " ")
        together[names] = hobby.replace("\n", "") if hobby else None

    with open(output_file, "w+", encoding="utf-8") as o_f:
        o_f.writelines(json.dumps(together))

    return sys.exit(0)

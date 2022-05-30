""" Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
 и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
 использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
 браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
 Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
 величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
 аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
 того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
 """

from datetime import datetime as dt
import requests
# from decimal import Decimal

site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

def currency_rates(currency):
    currency_code = currency.upper()

    if not currency_code in site.text:
        return None

    currency_val = site.text.split(currency_code)
    value = currency_val[1].split("</Value>")[0].split("<Value>")[1]
    value = int(value.replace(',',''))
    value = round((value / 10000), 2)
    date = site.headers["Date"]
    date = dt.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
    return f'{value}, {date}'

print((currency_rates("Aud")))

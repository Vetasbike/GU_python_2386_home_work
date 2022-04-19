""" Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
 в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
 Убедиться, что ничего лишнего не происходит.
"""
from datetime import datetime as dt
import requests

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
    return value, date

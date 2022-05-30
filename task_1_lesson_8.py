"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError
"""

import re

def email_parse(email_address):
    pars = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)

    if not pars:
        raise ValueError(f"wrong email: {email_address}")
    return print(dict(zip(["username", "domain"], pars[0])))

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')

"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
>> num_translate("one")
"один"
>> num_translate("eight") dictionary
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.

"""
dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четире',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять'
}
def num_translate(english_word):
    return dictionary.get(english_word)

def num_translate_adv(english_word):
    eng_word = dictionary.get(english_word.lower())
    if eng_word:
        return eng_word.capitalize() if english_word[0].isupper() else eng_word
    return None

print(num_translate('two'))
print(num_translate_adv('Two'))

"""
Задание №7
✔ Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в
строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ — символ,
а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
"""

print(f'С использованием count:')


def char_dict(text: str) -> dict[str:int]:
    return {char: text.count(char) for char in text}


text_1 = 'Москва - столица нашей Родины'

[print(f'{key}: {value}') for key, value in char_dict(text_1).items()]


print(f'\nБез использования count')
text_2 = 'Москва - столица нашей Родины'

dict_of_char = {}
for i in text_2:
    if i in dict_of_char.keys():
        dict_of_char[i] += 1
    else:
        dict_of_char[i] = 1
print(dict_of_char)

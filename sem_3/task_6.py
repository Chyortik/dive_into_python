"""
Задание №6 Пользователь вводит строку текста.
Вывести каждое слово с новой строки.
- Строки нумеруются начиная с единицы.
- Слова выводятся отсортированными согласно кодировки Unicode.
- Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


list_1 = 'Строки нумеруются начиная с единицы'
res = sorted(list_1.split())
[print(f'{i} - {word:>{len(max(res, key=len))}}') for i, word in enumerate(res, 1)]

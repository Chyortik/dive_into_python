"""
Задание №4
- Создайте вручную список с повторяющимися элементами.
- Удалите из него все элементы, которые встречаются дважды.
"""


list_1 = [4, 2, 4, 2, 5, 7, 8, 5, 7, 3]
print(list(filter(lambda x: list_1.count(x) != 2, list_1)))

"""
Задание №5
- Создайте вручную список с повторяющимися целыми числами.
- Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
- Нумерация начинается с единицы.
"""


list_1 = [7, 3, 5, 14, 6, 5]
print([i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(list_1, 1))])

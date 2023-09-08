"""
Задание №1. Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

a = 28
b = 'string'
c = (1, 7, 4, 10, 12)
d = {1: 'one', 2: 'two'}
e = [5, 8, 6, 5, 9, 6, 8, 7, 4, 2, 5, 1, 2]
print(f' a - {type(a)},\n b - {type(b)},\n c - {type(c)},\n d - {type(d)},\n e - {type(e)}')

"""
Вывод:
 a - <class 'int'>,  
 b - <class 'str'>,  
 c - <class 'tuple'>,
 d - <class 'dict'>, 
 e - <class 'list'>  
"""
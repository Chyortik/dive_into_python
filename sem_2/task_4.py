"""
Напишите программу, которая вычисляет площадь круга
и длину окружности по введённому диаметру.
Диаметр не превышает 1000 у.е.
Точность вычислений должна составлять не менее 42 знаков после запятой.
"""

from math import pi
import decimal

decimal.getcontext().prec = 42
_pi = decimal.Decimal(pi)

while True:
    d: int = int(input('Введите значение диаметра окружности: '))
    if d > 1000:
        print('Введите значение до 1000')
        continue
    else:
        s = (_pi * d ** 2) / 4
        l = _pi * d
        print(f'Площадь круга равна {s}')
        print(f'Длина окружности равна {l}')
        break
    
        

"""
Вывод
Введите значение диаметра окружности: 1111
Введите значение до 1000
Введите значение диаметра окружности: 100
Площадь круга равна 7853.98163397448278999490867136046290397645
Длина окружности равна 314.159265358979311599796346854418516159058
"""
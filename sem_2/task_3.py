"""
Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата, а
не для решения.
Дополнительно: 
Попробуйте избежать дублирования кода в преобразованиях
к разным системам счисления.
Избегайте магических чисел.
Добавьте аннотацию типов, где это возможно.
"""

def num_convert(num: int, mode: str) -> str:
    result = ''
    convert: int = 2

    match mode:
        case 'bin':
            convert = 2
        case 'oct':
            convert = 8

    while num >= 1:
        res = num % convert

        result += str(res)
        num = num // convert

    return result[::-1]


a = int(input('Введите число: '))
print(f'Двоичное представление введенного числа: {num_convert(a, mode="bin")}, Проверка: {bin(a)}')
print(f'Восьмеричное представление введенного числа: {num_convert(a, mode="oct")}, Проверка: {oct(a)}')


"""
Вывод:
Введите число: 100
Двоичное представление введенного числа: 1100100, Проверка: 0b1100100
Восьмеричное представление введенного числа: 144, Проверка: 0o144
"""

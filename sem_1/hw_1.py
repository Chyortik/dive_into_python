print('\nТреугольник существует только тогда, когда сумма любых двух его сторон больше третьей')
a = int(input('\nВведите длину стороны а: '))
b = int(input('\nВведите длину стороны b: '))
c = int(input('\nВведите длину стороны c: '))
res = ''
if a + b > c and b + c > a and a + c > b:
    res = 'Треугольник существует'
    if a == b == c:
        res = 'Треугольник равносторонний'
    elif a == b or b == c or c == a:
        res = 'Треугольник равнобедренный'
    else:
        res = 'Треугольник разносторонний'
else:
    res = 'Такого треугольника не существует'
print(f'\nОтвет: {res}\n')
MIN = 0
MAX = 100000

num = int(input(f'\nВведите число от {MIN} до {MAX}: '))
divider = 2
count = 0

if MIN <= num <= MAX:
    for i in range(divider, num - 1):
        if num % i == 0:
            count += 1
    if count <= 0:
        res = '\nЧисло является простым\n'
    else:
        res = '\nЧисло является составным\n'
else:
    res = '\nВведённое число не входит в заданный диапазон\n'

print(count)
print(res)

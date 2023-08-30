from random import randint

print('\nВас приветствует программа "Угадай число за 10 попыток!"')

LOWER_LIMIT = 0
UPPER_LIMIT = 100
COUNT_TRY = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
is_win = True
for _ in range(COUNT_TRY):
    number = int(input('\nВведи число от 0 до 100: '))
    if number > num:
        print('\nВаше число БОЛЬШЕ загаданного\n')
        is_win = False
        COUNT_TRY -=1
        print(f'Осталось попыток: {COUNT_TRY} ')
    elif number < num:
        print('\nВаше число МЕНЬШЕ загаданного\n')
        is_win = False
        COUNT_TRY -=1
        print(f'Осталось попыток: {COUNT_TRY} ')
    else:
        print('\nВы выиграли!\n')
        is_win = True
        break
if not is_win:
    print('\nК сожалению вы проиграли\n')
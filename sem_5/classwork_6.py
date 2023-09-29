def mult_table():
    LOWER_LIMIT = 2
    UPPER_LIMIT = 10
    COLUMN = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_LIMIT and k == i + COLUMN - 1
            else f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1
            else f'{k:>} x {j:>2} = {k * j:>2}\t\t'
            for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
            for k in range(i, i + COLUMN)))


if __name__ == '__main__':
    mult_table()

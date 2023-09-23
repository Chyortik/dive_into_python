def matrix_transposition(*a_list: list[[int]]) -> list[()] | str:
    is_transposition = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transposition = False
    if is_transposition:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспонировать'


print(matrix_transposition([1, 2], [3, 4]))
print(matrix_transposition([1, 2], [3, 4, 5]))
print(matrix_transposition([1, 1], [2, 2]))
print(matrix_transposition([1, 2, 3], [4, 5, 6]))

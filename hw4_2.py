"""✔ Напишите функцию для транспонирования матрицы
"""

import numpy as np


def transpose_matrix(matr):
    rows = len(matr)
    columns = len(matr[0])
    result = [[0 for _ in range(rows)] for __ in range(columns)]
    for i in range(columns):
        for j in range(rows):
            result[i][j] = matr[j][i]
    return result


def print_two_d_matrix(matr):
    for i in range(len(matr)):
        for j in range(len(matr[0]) - 1):
            print(f'{matr[i][j]:3}', end=' ')
        print(f'{matr[i][j + 1]:3}')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print_two_d_matrix(matrix)
print()
print_two_d_matrix(transpose_matrix(matrix))
print()
print_two_d_matrix(np.array(matrix).transpose())  #проверка

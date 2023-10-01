"""✔ Напишите функцию для транспонирования матрицы
"""


class Matrix:

    def __init__(self, mtx_list: list):
        self.mtx = mtx_list

    def get_matrix(self):
        return self.mtx

    def transpose_matrix(self):
        return list(zip(*self.mtx))

    def matrix_to_string(self):
        return '\n'.join(str(tuple(x)) for x in self.mtx)

    def transposed_matrix_to_string(self):
        return '\n'.join(str(x) for x in self.transpose_matrix())


if __name__ == '__main__':
    matrix_example = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])
    print(matrix_example.matrix_to_string())
    print(matrix_example.transpose_matrix())
    print(matrix_example.transposed_matrix_to_string())


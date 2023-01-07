"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
"""

matrix_01 = [[1, 2, 3], [3, 2, 1]]
matrix_02 = [[4, 5, 6], [6, 5, 4]]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        str_matrix = (item for item in self.matrix)
        while True:
            try:
                print(next(str_matrix))
            except StopIteration:
                break

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            result_matrix = [[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)] for row_1, row_2 in
                             zip(self.matrix, other.matrix)]
            return f'Результат сложения двух матриц, {self.matrix} & {other.matrix}: {result_matrix}'
        else:
            return 'Нельзя суммировать матрицы разной длины'


a = Matrix(matrix_01)
b = Matrix([[4, 5, 6], [6, 5, 4]])

a.__iter__()
print(a + b)

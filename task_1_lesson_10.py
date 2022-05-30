"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
"""
class Matrix:
    def __init__(self, data:list) -> None:
        self.data = data

    def __str__(self) -> None:
        result = []
        for i in self.data:
            result.append(' '.join([str(x) for x in i]))
        return '\n'.join(result)

    def __add__(self, other) -> None:
        if len(self.data) == len(other.data):
            result = []
            for i, b in enumerate(self.data):
                new_list = list(map(lambda x, y: x + y, b, other.data[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return

lists1 = [[31, 32], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
lists2 = [[31, 32], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]

matrix1 = Matrix(lists1)
matrix2 = Matrix(lists2)
matrix = matrix1 + matrix2

print(matrix)

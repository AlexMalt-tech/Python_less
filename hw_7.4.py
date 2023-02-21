"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, param_1):
        self.param_1 = param_1

    def __add__(self, param_2):
        return Matrix(self.param_1 + param_2.param_1)

    def print_matrix(self):
        for el in self.param_1:
            for unt in el:
                print(unt, end=' ')
            print()

    def __str__(self):
        return f'{self.print_matrix()}'


matrx_2 = Matrix([[2, 2, 2], [2, 2, 2]])
matrx_1 = Matrix([[1, 1, 1], [1, 1, 1]])

matrx_3 = matrx_1.__add__(matrx_2)

print(matrx_3)

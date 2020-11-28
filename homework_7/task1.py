# coding: utf-8
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    matrix = list()

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        out = ''
        for col in self.matrix:
            out += " ".join(map(str, col)) + "\n"
        return out

    def __add__(self, other):
        # if len(self.matrix) != len(other.matrix):
        all = []
        for i in range(len(self.matrix)):
            m1c = self.matrix[i]
            m2c = other.matrix[i]
            alist = []
            # print(col, other_col)
            for (item1, item2) in zip(m1c, m2c):
                alist.append(item1 + item2)
            all.append(alist)
        return Matrix(all)

m1 = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
m2 = Matrix([[4, 4, 4], [3, 3, 3], [2, 2, 1]])
# print(m1)
print(m1+m2)


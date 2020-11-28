# coding: utf-8

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух
# клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида
# *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки
# равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****. Подсказка:
# подробный список операторов для перегрузки доступен по ссылке.


class Cell(list):
    def __init__(self, cell):
        super(Cell, self).__init__()
        self.cell = cell

    def __add__(self, other):
        print(f"Add\n{Cell(self.cell)} + \n{Cell(other.cell)}Result:")
        all = []
        for i in range(len(self.cell)):
            m1c = self.cell[i]
            m2c = other.cell[i]
            alist = []
            for (item1, item2) in zip(m1c, m2c):
                alist.append(item1 + item2)
            all.append(alist)
        return Cell(all)

    def __str__(self):
        out = ''
        for col in self.cell:
            out += " ".join(map(str, col)) + "\n"
        return out

    def __sub__(self, other):
        print(f"Substract\n{Cell(self.cell)} - \n{Cell(other.cell)}Result:")
        all = []
        for i in range(len(self.cell)):
            m1c = self.cell[i]
            m2c = other.cell[i]
            alist = []
            for (item1, item2) in zip(m1c, m2c):
                alist.append(item1 - item2)
            all.append(alist)
        return Cell(all)

    def __mul__(self, other):
        print(f"Multiply\n{Cell(self.cell)} x \n{Cell(other.cell)}Result:")
        all = []
        for i in range(len(self.cell)):
            m1c = self.cell[i]
            m2c = other.cell[i]
            alist = []
            for (item1, item2) in zip(m1c, m2c):
                alist.append(item1 * item2)
            all.append(alist)
        return Cell(all)

    def __truediv__(self, other):
        print(f"Divide\n{Cell(self.cell)} / \n{Cell(other.cell)}Result:")
        all = []
        for i in range(len(self.cell)):
            m1c = self.cell[i]
            m2c = other.cell[i]
            alist = []
            for (item1, item2) in zip(m1c, m2c):
                alist.append(item1 / item2)
            all.append(alist)
        return Cell(all)

    def make_order(self):
        pass


c1 = Cell([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
c2 = Cell([[4, 4, 4], [3, 3, 3], [2, 2, 1]])
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
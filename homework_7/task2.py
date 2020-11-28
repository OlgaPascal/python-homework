# coding: utf-8
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.
#

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc_expenses(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def calc_expenses(self):
        return self.V / 6.5 + 0.5

    @property
    def v(self):
        return self.V

    @property
    def expenses(self):
        return f"Expenses: {self.calc_expenses()}"

    def __str__(self):
        return 'Coat, size:' + str(self.V)


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def calc_expenses(self):
        return 2 * self.H + 0.3

    @property
    def expenses(self):
        return f"Expenses: {self.calc_expenses()}"

    @property
    def h(self):
        return self.H

    def __str__(self):
        return 'Suite, size:' + str(self.H)


c = Coat(10)
print(c.v)
print(c.calc_expenses())
print(c.expenses)

s = Suit(2)
print(s.h)
s.calc_expenses()
print(s.expenses)



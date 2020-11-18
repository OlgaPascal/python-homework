# coding: utf-8

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from functools import reduce


# solution 1
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        yield fact


# # solution 1
for el in fact(4):
    print(el)


# solution 2
def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# test if solution works
# import math
# print(fact(4) == math.factorial(4) )
# print(fact(5) == math.factorial(5))
# print(fact(7) == math.factorial(7))

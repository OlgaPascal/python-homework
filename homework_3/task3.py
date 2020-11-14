# coding: utf-8
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    print(sum(sorted([a,b,c], reverse=True)[:2]))

my_func(4,8,9)
my_func(14,8,9)




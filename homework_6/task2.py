# coding: utf-8
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1
# см * чи сло см толщины полотна. Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т
#


class Road:
    __lenght = float
    __width = float
    __depth = float
    __weight_per_sq_m = 25

    # def cm_to_m(self, cm):
    #     return cm/100

    def weight_in_ton(self):
        return self.weight() / 1000

    def weight(self):
        return self.__lenght * self.__width * self.__weight_per_sq_m * self.__depth

    def __init__(self, length, width, depth):
        """
        :param length: in meters
        :param width: in meters
        :param depth: in cm
        """
        self.__lenght = length
        self.__width = width
        # self.__depth = self.cm_to_m(depth)
        self.__depth = depth


road = Road(length=5000, width=20, depth=5)
print(road.weight())
print(road.weight_in_ton())

assert road.weight_in_ton() == 12500

# coding: utf-8
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для
# каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title = str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Ручка - Запуск отрисовки.")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш - Запуск отрисовки.")


class Handle(Stationery):
    def draw(self):
        print("Маркер - Запуск отрисовки.")


p = Pen()
p.draw()

pencil = Pencil()
pencil.draw()

h = Handle()
h.draw()

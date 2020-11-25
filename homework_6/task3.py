# coding: utf-8
# 3.
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = str
    surname = str
    position = str
    __income = dict(wage=0, bonus=0)

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def set_income(self, wage, bonus):
        self.__income = dict(wage=wage, bonus=bonus)

    def get_income(self):
        return self.__income


class Position(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.get_income()['wage'] + self.get_income()['bonus']


john = Position(name="John", surname="Doe", position="engineer")
john.set_income(20000, 5000)
print(john.get_full_name())
print(john.get_total_income())

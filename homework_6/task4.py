# coding: utf-8
# 4. Реализуйте базовый класс Car. У
# данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры
# классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и
# также покажите результат.


class Car:
    speed = float
    color = str
    name = str
    is_police = bool
    direction = str

    def go(self):
        print(f"{self.color} {self.name} Go..")

    def stop(self):
        print(f"{self.color} {self.name} stoped.")

    def turn(self, new_direction):
        self.direction = new_direction
        print(f"{self.color} {self.name} turned to {new_direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} speed {self.speed}")
        return self.speed

    def set_direction(self, direction):
        print(f"{self.color} {self.name} turned to {direction}")
        self.direction = direction

    def get_direction(self):
        return self.direction

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police


class TownCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            return "Превышена скорость"

        return super().show_speed()


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 40:
            return "Превышена скорость"
        return super().show_speed()


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


taxi = TownCar(speed=45, color="yellow", name="toyota", is_police=False)
taxi.go()
taxi.set_direction("east")
taxi.show_speed()
taxi.turn("north")
taxi.stop()

ferrari = SportCar(speed=245, color="red", name="ferrari", is_police=False)
ferrari.go()
ferrari.set_direction("west")
ferrari.show_speed()
ferrari.turn("south")
ferrari.stop()

minibus = WorkCar(speed=55, color="yellow", name="mercedes", is_police=False)
minibus.go()
minibus.set_direction("south")
minibus.show_speed()
minibus.turn("west")
minibus.stop()

police = PoliceCar(speed=155, color="black", name="ford", is_police=True)
police.go()
police.set_direction("south")
police.show_speed()
police.turn("west")
police.stop()

# coding: utf-8
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from time import sleep


class TrafficLight():
    RED = dict(color="red", pause=7)
    GREEN = dict(color="green", pause=2)
    YELLOW = dict(color="yellow", pause=1)
    __color = RED
    running_sequence = [RED, GREEN, YELLOW]

    def running(self):
        for color in self.running_sequence:
            yield color['color']
            sleep(color['pause'])


t = TrafficLight()
for color in t.running():
    print(color)

# testing
correct_sequence = [t.RED, t.GREEN, t.YELLOW]
correct_sequence.reverse()
for color in t.running():
    assert color == correct_sequence.pop()['color']

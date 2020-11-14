# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.


typename = ['somestring', 348, 454.34, complex(2,3), ["1", "2"], ('aaa', 'bbb'),
     set('test'), frozenset('2wewfwfwefwef'), {1: "one", 2: "two"},
     True, b'text', bytearray(b"some text"), None]


for element in typename:
    print (type(element))


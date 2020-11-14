# coding: utf-8

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(firstname, lastname, birthday, city, email, phone):
    print(f"{firstname}\n{lastname}\n{birthday}\n{city}\n{email}\n{phone}")

user(firstname="Ivan",lastname="Pascal", birthday='2005', city='Chisinau', email='some@gmail.com', phone='+3731234567')



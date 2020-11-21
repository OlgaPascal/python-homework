# coding: utf-8

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task1.txt", "w", encoding="utf-8") as fw:
    user_data = " "
    while user_data != "":
        user_data = input("Enter data:")
        fw.write(user_data + "\n")

# coding: utf-8

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
word_map = {
    'One': 'Один',
    'Two': "Два",
    'Three': "Три",
    'Four': 'Четыре'
}
fw = open("task4-out.txt", "w", encoding="utf8")
with open("task4.txt", "r", encoding="utf-8") as fr:
    for i in fr:
        col1 = i.split("-")[0].strip()
        col2 = i.split("-")
        col2[0] = word_map[col1]
        print(col2)
        fw.write(" -".join(col2))
fw.close()

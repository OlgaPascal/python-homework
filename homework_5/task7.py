# coding: utf-8

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

with open("task7.txt", encoding="utf-8", mode="r") as fr:
    firms = []
    profitable_firms = []
    nonprofitable_firms = []
    attrs = ['name', 'prop_type', 'income', 'outcome']
    for l in fr.readlines():
        firm = {attrs[i]: j for i, j in enumerate(l.split())}
        av_profit = float(firm['income']) - float(firm['outcome'])
        f = [firm, {"average_profit": av_profit}]
        firms.append(f)
        if av_profit > 0:
            profitable_firms.append(f)
        else:
            nonprofitable_firms.append(f)

    average_profit = sum([sv[1]['average_profit'] for sv in profitable_firms]) / len(profitable_firms)
    print(f"All companies average profit: {average_profit}")
    print(firms)

with open("task7.json", encoding="utf-8", mode="w") as fw:
    json.dump(firms, fw, ensure_ascii=False)
    print("Data saved to file")

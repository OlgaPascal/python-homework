# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

selected_month = int(input("Enter month number 1-12: ")) - 1

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November",
              "December"]
print(month_list[selected_month])

d = {}
for el in month_list:
    d[month_list.index(el)] = el
print(d[selected_month])

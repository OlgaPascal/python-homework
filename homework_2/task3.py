# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    selected_month = int(input("Enter month number 1-12: "))
    times = {"winter": [12, 1, 2], "spring": [3,4,5], "summer": [6,7,8], "autumn": [9,10,11]}

    for time, months in times.items():
        if selected_month in months:
            print(time)
    # let's print month name










    # d = {}
    # month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    #               "November", "December"]
    # for month in month_list:
    #     d[month_list.index(month)] = month
    # print(d[selected_month-1])
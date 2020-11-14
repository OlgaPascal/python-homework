# name = "Olga"
# age = "39"
# print("My name is ", name, "My age is ", age)
# a = int(input(f"Enter the first number for"))
# print(type(a))
#
# print(a + 10)
# print("The number is OK")
# print(f" you entered {a}")
# b = input("Enter some string")
# print(f"you entered {b}")
#
# print(f"ljdfglkdjfglkdfjg dglkdjfglkdjfg dflgkdj {b} ")
# print(" some string information not dynamic ")
#
# # task 2
# seconds = int(input("Enter seconds"))
# hour = seconds // 3600
# minute = seconds // 60
# print(f"Time is {hour:02}:{minute:02}:{seconds:02}")
#
# # task 3
# number = int(input("Enter number: "))
# a = 2 * "{}".format(number)
# b = 3 * "{}".format(number)
# sum = number + int(a) + int(b)
# print("{} {} {} {}".format(number, a, b, sum))
#
# # task 4
# number = str(input("Enter min 4-digit number : "))
# sp = [n for n in number]
# print(max(sp))
#
# # task5
# profitability = 0
# profit = int(input("Enter profit value"))
# expenses = int(input("Enter expenses"))
# if profit > expenses:
#     profitability = profit - expenses
#     pty = profitability / profit
#     print(f"Company is profitable, the profitability is {pty}")
# else:
#     print("Company is not profitable")
#     members = int(input("Company members number: "))
#     permember = profitability / members
#     print(f"Member salary would be: {permember}")
#
#
# task6

first_day_result = int(input("Enter result for day 1: "))
challenge = int(input("Enter challenge in km: "))
day = 1
prev_day_result = first_day_result
each_day_result = first_day_result
while each_day_result < challenge:
    each_day_result = prev_day_result + (prev_day_result / 100 * 10)
    day += 1
    prev_day_result = each_day_result
    print(f"{each_day_result} day {day}")
print(f"Result will be achieved on {day} day")

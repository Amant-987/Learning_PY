# В некоторой школе решили набрать
# три новых математических класса и
# оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт,
# которое нужно приобрести для них.
#
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

a = int(input("Enter count of people: "))
b = int(input("Enter count of people: "))
c = int(input("Enter count of people: "))

total_students = a + b + c
desks_needed = (total_students + 1) // 2

print(desks_needed)
# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Enter big number: "))
k = 0
while 2**k <= N:
    print(2**k)
    k += 1
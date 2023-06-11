# 1. Дано натуральное число *N* и
# последовательность из *N* элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
#
# ***Примечание.*** В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# def reverse_sequence():
#     n = int(input())
#     if n == 0:
#         return
#     x = int(input())
#     reverse_sequence()
#     print(x)

def reverse_sequence(n):
    if n == 0:
        return
    x = int(input())
    reverse_sequence(n-1)
    print(x)

#
# Эта функция рекурсивно запрашивает у
# пользователя *n* чисел и выводит их в
# обратном порядке. Если *n* равно 0,
# то функция ничего не делает. Чтобы использовать
# эту функцию, нужно вызвать ее с нужным аргументом *n*:


n = int(input("Введите количество элементов: "))
reverse_sequence(n)
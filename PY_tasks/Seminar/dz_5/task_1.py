# Задача 26:  Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень
# B с помощью рекурсии.
#
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def power(nummer,grad):
    if grad ==0:
        return 1
    elif grad % 2 ==0:
        return power(nummer,grad//2)**2
    else:
        return nummer*power(nummer,grad-1)

nummer = int(input("Enter number: "))
grad = int(input("Enter degree: "))
print(f"Degree {grad} of number {nummer} is {power(nummer,grad)}")
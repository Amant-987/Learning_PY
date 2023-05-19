# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = input("Enter third-digits number: ")
if len(num) == 3:
    print(f"Sum of digits {num} is {int(num[0])+int(num[1])+int(num[2])}")
else:
    print("Not third-digits number!")

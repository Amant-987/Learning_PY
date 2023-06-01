# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
#

first_len = int(input("Enter number of length for the first set: "))
second_len = int(input("Enter number of length for the second set: "))
first_set = set()
second_set = set()
for i in range(first_len):
    first_set.add(int(input(f"Enter {i+1} element for the first set: ")))

for i in range(second_len):
    second_set.add(int(input(f"Enter {i+1} element for the second set: ")))

result_set = first_set.union(second_set).difference(first_set.intersection(second_set))
print(sorted(first_set))
print(sorted(second_set))
print("Ihr Resultat aus einzelnen Zahlen in aufsteigender Reihenfolge:")
print(sorted(result_set))

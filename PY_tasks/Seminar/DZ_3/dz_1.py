# Задача 16: Требуется вычислить, сколько раз
# встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

quantity_el = int(input("Enter quantity elements in array: "))
my_array = list(map(int, input("Enter numbers for array with SPACE: ").split(" "))) #read our array
find_num = int(input("Enter number for find: "))

count = 0
for i in range(quantity_el):
    if my_array[i] == find_num:
        count +=1

print(f"Number {find_num} entered {count} times.")
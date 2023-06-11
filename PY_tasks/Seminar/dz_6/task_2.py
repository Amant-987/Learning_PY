# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def find_ind(my_array, min_val, max_val):
    indexes = []
    for i in range(len(my_array)):
        if min_val <= my_array[i] <= max_val:
            indexes.append(i)
    return indexes

my_array = [random.randint(0,100) for i in range(10)]
min_val = random.randint(0, 50)
max_val = random.randint(50, 100)

print("My array: ", my_array)
print("Range: ", min_val," - ", max_val)
print("Indexes of elements belonging to the range: ", find_ind(my_array, min_val, max_val))

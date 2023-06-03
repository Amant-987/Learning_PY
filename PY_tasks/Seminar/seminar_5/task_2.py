# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

grades = [5, 4, 1, 5, 2, 5, 3, 4, 5, 4, 1, 5, 1, 1]  # пример списка оценок
print(grades)
min_grade = min(grades)  # находим минимальную оценку
max_grade = max(grades)  # находим максимальную оценку
for i in range(len(grades)):
    if grades[i] == max_grade:
        grades[i] = min_grade  # заменяем максимальную оценку на минимальную
print(grades)  # выводим измененный список оценок
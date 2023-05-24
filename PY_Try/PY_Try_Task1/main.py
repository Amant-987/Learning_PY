# написать программу,
# которая загружает текстовый файл и
# анализирует количество букв в данном тексте
# (учитываются только буквы без цифр и знаков препинаний).
# Результат вывести в алфавитном порядке в виде
# горизонтальной гистограммы (в процентном соотношении)

import string

# Открываем файл и считываем его содержимое
with open('file.txt', 'r') as file:
    text = file.read()

# Удаляем знаки препинания и цифры из текста
text = text.translate(str.maketrans('', '', string.punctuation + string.digits))

# Создаем словарь для хранения количества букв
letters_count = {}

# Перебираем все буквы в тексте и увеличиваем счетчик для каждой буквы
for letter in text:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

# Считаем общее количество букв в тексте
total_letters = sum(letters_count.values())

# Выводим результаты в алфавитном порядке
for letter in sorted(letters_count.keys()):
    count = letters_count[letter]
    percentage = count / total_letters * 100
    print(f"{letter}: {'*' * int(percentage)} ({percentage:.2f}%)")
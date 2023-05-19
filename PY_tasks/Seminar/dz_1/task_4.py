# Задача 8: Требуется определить, можно ли от шоколадки
# размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Enter quantity of rows: "))
m = int(input("Enter quantity of columns: "))
k = int(input("Enter quantity of pieces: "))
if (m * n < k):
    print("No chances!")
elif k % n == 0 or k % m == 0:
    print("Of course!")
else:
    print("Nope!")

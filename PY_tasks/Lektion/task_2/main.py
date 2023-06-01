# # # # # list_1 = [1,2,3,4,5,6,7,8,9,"=))"]
# # # # # # print(*list_1)
# # # # # # * before list_1 - open list without brackets
# # # # #
# # # # # for i in list_1:
# # # # #     print(i)
# # # # #
# # # # # print(len(list_1))
# # # # # print(list_1[9])
# # # # # print(list_1[-2])  #indexing from END
# # # # #
# # # # # list_2 = [1,2,3,6]
# # # # # print(list_2)
# # # # # list_2.append(8)
# # # # # print(list_2)
# # # #
# # # # list_1 = []
# # # # for i in range(10):
# # # #     list_1.append(i)
# # # #     print(list_1)
# # # #
# # # # print(list_1.pop())
# # # # temp = list_1.pop(2)
# # # # print(list_1)
# # # # print(temp)
# # # # # pop() - picks up last element from list
# # # # # pop(i) = picks up element with index i
# # # # list_1.insert(2,24)
# # # # # insert - input new element, 2 - index, 24 - element for input
# # # # print(list_1)
# # # # print(list_1[:2])
# # # # print(list_1[2:])
# # # # print(list_1[2:6])
# # #
# # # # t - () - empty kortege
# # # t = ()
# # #
# # # print(type(t))
# # # t = (1,5,4,) # comma at the end!
# # # print(type(t))
# # # list_1 = [1,2,3]
# # # print(list_1)
# # # kortege = tuple(list_1)
# # # print(kortege)
# # # # a,b = 1,2 - multiple enter
# # # a,b,c = list_1
# # # print(a,b,c)
# # #
# # # list_2 = (1,2,3,4,5,)
# # # for i in range(len(list_2)):
# # #     print(list_2[i])
# #
# # # dictionary = {}
# # # dictionary = dict()
# # # dictionary['q'] = 'qwerty'
# # # print(dictionary)
# # # dictionary['w'] = 'werty'
# # # print(dictionary)
# # dictionary = {}
# # dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # # print(dictionary['left']) # ← типы ключей могут отличаться
# # # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # # dictionary['left'] = '⇐'
# # # print(dictionary['left']) # ⇐
# # # print(dictionary['type']) # KeyError: 'type'
# # # del dictionary['left'] # удаление элемента
# # # for item in dictionary:
# # #     print(item)
# # #     print('{}:{}'.format(item, dictionary[item]))
# # for (k,v) in dictionary.items():
# #     print(k,v)
#
# # # 3 in mnogestva - only unic item
# # colors = {'red', 'green', 'blue'}
# # print(colors) # {'red', 'green', 'blue'}
# # colors.add('red')
# # print(colors) # {'red', 'green', 'blue'}
# # colors.add('gray')
# # print(colors) # {'red', 'green', 'blue','gray'}
# # colors.remove('red')
# # print(colors) # {'green', 'blue','gray'}
# # # colors.remove('red') # KeyError: 'red'
# # colors.discard('red') # ok - checked values for delete and delete it
# #
# # colors.clear() #clean values
# # q = set()
# #
# # a = {1, 2, 3, 5, 8}
# # b = {2, 5, 8, 13, 21}
# # c = a.copy() # c = {1, 2, 3, 5, 8}
# # u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# # i = a.intersection(b) # i = {8, 2, 5}
# # dl = a.difference(b) # dl = {1, 3}
# # dr = b.difference(a) # dr = {13, 21}
# # q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
#
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
#
# print(b)

list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1)
# 2. Добавить условие (только чётные числа)
list_2 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_3 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_4 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
print(list_2)
print(list_3)
print(list_4)

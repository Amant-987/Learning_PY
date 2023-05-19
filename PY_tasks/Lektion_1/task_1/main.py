# n = 1.89
# print(n)
# m='kj"hjg"h'
# print(m)
# c="ky\'ut"
# print(c)
# print(type(n))
# #print(type(n))
# '''print(type(n))
# print(type(n))'''
# a=5
# b=5.89
# c='hello'
# print(a,'-',b,'-',c)
# print(f"{a} - {b} - {c}")
# print("{}-{}-{}".format(a,b,c))
# print('Enter first row:')
# a=input()
# # b=input("Enter second number:")
# # print(a,"+",b,"=", a+b)
# c=5.89
# print(c)
# print(type(c))
# c=str(c)
# print(c)
# print(type(c))
# c=1
# print(c)
# print(type(c))
# c=bool(c)
# print(c)
# print(type(c))
# print("Enter first row:")
# a = int(input())
# b = int(input("Enter second number:"))
# print(a, "+", b, "=", a + b)

"""
priority of math func:
1 - exponentiation (**)
2 - multiplication (*)
3 - division (/)
4 - division without remainder (//)
5 - remainder of division (%)
6 - addition (+)
7 - subtraction (-)
"""
# a = 5.2345
# b = 5.567
# print(round(a * b, 2))
# # round(1.23446, 3)
"""
iteration

iter = 2
iter += 3
iter += 4
iter /= 5
iter //= 5
iter %= 5
iter **= 5
"""
# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = "qwe"
# b = "qwe"
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input("Schreibe dich Name: ")
# if username == "Aleks":
#     print("Naja! Das ist Aleks!")
# elif username == "Alex":
#     print("Das ist Aleks auch!")
# elif username == "Anya":
#     print("Anya ist Meine Frau!")
# else:
#     print("Hello, ", username)

# i = 0
# while i < 5:
#     if i == 3:
#         break #not used
#     i += 1
# else:
#     print("Done")
#     print("Break")
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag: #  (while flag:) = (while flag=True:)
#     if n % i == 0:  # if delimiter = 0
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# r = range() func - give counting with step +1
# r = range(5) 0 1 2 3 4
# r = range(2,5) 2 3 4
# r = range(0,-5) ---
# r = range(1,10,2) 1 3 5 7 9
# r = range(100,0,-20) 100 80 60 40 20

# r = range(100,0,-20)
# for i in r:  --- or  ---  for i in range(100,0,-20):
#       print(i)
#  100 80 60 40 20

# a = "qwerty"
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = "SprachHAndlungen könNen aLs direkte und indirekte dargestellt werden"
# print(len(text))
# print("werden" in text)
# print(text.lower())
# print(text.upper())
# print(text.replace("und", "UND"))
# print(text[0])
# print(text[len(text)-1])
# print(text[-1])
# print(text[:])
# print(text[:2]) - like range() func
# print(text[20:])
# print(text[10:20])
# print(text[10:-18])
# print(text[0:len(text):6]) - avg 6 element from row
# print(text[::6])- avg 6 element from row from start
# text = text[2:9] + text[-5]+text[:2]
# print(text)

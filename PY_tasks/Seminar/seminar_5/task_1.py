# 1. Последовательностью
# Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonacci(n):
    if n == 0: # or if n in [0,1] return n
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number of value Fibonacci: "))
print("N of value Fibonacci: ", fibonacci(n))


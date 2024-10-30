x = int(input("Введите число x: "))
n = int(input("Введите число n: "))

alpha = x**n

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

k = alpha/fac(n) 

print(k)
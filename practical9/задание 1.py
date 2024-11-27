x = int(input("Введите число x: "))
N = int(input("Введите число n: "))


def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

alpha = x**N

print(alpha / fac(N))

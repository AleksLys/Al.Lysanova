x = int(input("Введите двузначное число "))
n = x // 10

if n % 2 ==0:
    print(n, "чётное")
else:
    print(n, "нечётное")

g = x % 10

if g % 2 ==0:
    print(g, "чётное")
else:
    print(g, "нечётное")

x = float(input("Введите точку: "))

h = float(0.0)
e = float(0.5)
l = float(5.0)
p = float(5.5)

if x == h or x > h:
    if x == e or x > e or x < e:
        if x == l or x > l or x < l:
            if x == p or x < p:
                print("Точка принадлежит квадрату.")
            else:
                print("Точка не принадлежит квадрату.")

else:
    print("Точка не принадлежит квадрату.")

import math
m = int(input("Выберите фигуру:\n1-круг, 2-прямоугольник/квадрат, 3-треугольник\n"))

circle = 1   #круг
square = 2   #кв. 
triangle = 3 #треуг.

x = int(input("Введите сторону x:\n"))
y = int(input("Введите сторону y:\n"))
z = int(input("Введите сторону z:\n"))
if m==circle:
    s1 = 0.785 * x
    print("Площадь фигуры = {:.2f}".format(s1))
else:
    if m==square:
        s2 = x*y
        print("Площадь фигуры = {:.2f}".format(s2))
    else:
        p = (x+y+z)/2
        s3 = math.sqrt(p*(p-x)*(p-y)*(p-z))
        print("Площадь фигуры = {:.2f}".format(s3))

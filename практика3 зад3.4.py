x = int(input("Введите число "))
simple = True

i = 2
if x > 1 or x == 1:
 while i < abs(x):
    if x % i == 0:
      simple = False
    i += 1
 if simple:
    print("Число простое")

 else:
    print("Число не простое")
else:
    print("Число не простое")

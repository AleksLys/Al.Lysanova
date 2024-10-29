elements = int(input("Введите количество элементов массива: "))
a = []
zeros = a.count(0)
mean = elements / (elements - zeros) 

for i in range(elements):
    print("Введите", i, "элемент: ")
    a.append(int(input()))
print("Исходный массив: ", a)

for i in range(elements):
    if a[i] == 0:
        a[i] = mean 
print("Полученный массив: ", a) 

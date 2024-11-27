# Вычислить сумму и число положительных элементов матрицы A[N, N], находящихся над главной диагональю

n = int(input("Введите кол-во строк и кол-во столбцов: "))
A = []

for i in range(n):
    B = []
    for j in range(n):
        print("Введите [", i, ", ", j,"] элемент")
        B.append(int(input()))
    A.append(B)

print("Исходный массив: ") # вывод массива
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()

S = 0
C = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i][j] > 0:
            S += A[i][j]
            C += 1

print("Число положительных элементов: ", C)
print('Сумма: ', S)

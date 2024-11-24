# Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно. 
B = []
N = int(input("Введите кол-во строк: "))
M = int(input("Введите кол-во столбцов: "))

for i in range(N):
    A = []
    for j in range(M):
        print("Введите [", i, ", ", j,"] элемент")
        A.append(int(input()))
    B.append(A)

print("Исходный массив: ")
for i in range(N):
    for j in range(M):
        print(B[i][j], end = ' ')
    print()

maximum = B[0][0]
minimum = B[0][0]
for i in range(N):
    for j in range(M):
        if maximum < B[0][j]:
            maximum = B[0][j]
        if minimum > B[0][j]:
            minimum = B[0][j]
print('Максимальный элемент в первой строке: ', maximum)
print('Минимальный элемент в первой строке: ', minimum)
for i in range(N):
    for j in range(M):
        if B[0][j] == maximum: B[0][j] = minimum
        elif B[0][j] == minimum: B[0][j] = maximum

maximum = B[1][0]
minimum = B[1][0]
for i in range(N):
    for j in range(M):
        if maximum < B[1][j]:
            maximum = B[1][j]
        if minimum > B[1][j]:
            minimum = B[1][j]
print('Максимальный элемент во второй строке: ', maximum)
print('Минимальный элемент во второй строке: ', minimum)
for i in range(N):
    for j in range(M):
        if B[1][j] == maximum: B[1][j] = minimum
        elif B[1][j] == minimum: B[1][j] = maximum

maximum = B[2][0]
minimum = B[2][0]
for i in range(N):
    for j in range(M):
        if maximum < B[2][j]:
            maximum = B[2][j]
        if minimum > B[2][j]:
            minimum = B[2][j]
print('Максимальный элемент в третьей строке: ', maximum)
print('Минимальный элемент в третьей строке: ', minimum)
for i in range(N):
    for j in range(M):
        if B[2][j] == maximum: B[2][j] = minimum
        elif B[2][j] == minimum: B[2][j] = maximum

print('Изменённый массив: ')
for i in range(N):
    for j in range(M):
        print(B[i][j], end = ' ')
    print()
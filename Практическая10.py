n = 4
A = []
file = open('D:\\Читать\\записи\\вузовское\\питон\\Практическа10\\Задание8.txt')

for i in file.readlines(): #заполн. массив
    n1 = int(i)
    A.append(n1)

A = [A]*n

maximum = A[0][0]
minimum = A[0][0]
for i in range(n):
    for j in range(n):
        if maximum < A[0][j]:
            maximum = A[0][j]
        if minimum > A[0][j]:
            minimum = A[0][j]
print('Максимальный элемент в первой строке: ', maximum)
print('Минимальный элемент в первой строке: ', minimum)
for i in range(n):
    for j in range(n):
        if A[0][j] == maximum: A[0][j] = minimum
        elif A[0][j] == minimum: A[0][j] = maximum

maximum = A[1][0]
minimum = A[1][0]
for i in range(n):
    for j in range(n):
        if maximum < A[1][j]:
            maximum = A[1][j]
        if minimum > A[1][j]:
            minimum = A[1][j]
print('Максимальный элемент во второй строке: ', maximum)
print('Минимальный элемент во второй строке: ', minimum)
for i in range(n):
    for j in range(n):
        if A[1][j] == maximum: A[1][j] = minimum
        elif A[1][j] == minimum: A[1][j] = maximum

maximum = A[2][0]
minimum = A[2][0]
for i in range(n):
    for j in range(n):
        if maximum < A[2][j]:
            maximum = A[2][j]
        if minimum > A[2][j]:
            minimum = A[2][j]
print('Максимальный элемент в третьей строке: ', maximum)
print('Минимальный элемент в третьей строке: ', minimum)
for i in range(n):
    for j in range(n):
        if A[2][j] == maximum: A[2][j] = minimum
        elif A[2][j] == minimum: A[2][j] = maximum

print()
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()

file_vivod = A

file_v = open('file_vivod.txt', 'w') 
file_v.write(str(file_vivod))
file_v.close()


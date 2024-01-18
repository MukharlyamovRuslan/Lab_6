import numpy as np
#Проверка на ошибку
num = int(input('Введите количество критериев: '))
while num <= 0:
    print('Ошибка!!!')
    num = int(input('Введите количество критериев: '))
#Создал матрицу для записи коэффициентов сравнения
matrix = np.eye(num)
a = 1
for i in range(a, num+1):
    for j in range(a+1, num+1):
        matrix[i-1][j-1] = round(float(input('Введите коэффициент сравнения К{0}-К{1}:'.format(i, j))), 3)
        while int(matrix[i-1][j-1]) <= 0 or matrix[i-1][j-1] >= 10:
            print('Ошибка!!!')
            matrix[i - 1][j - 1] = round(float(input('Введите коэффициент сравнения К{0}-К{1}:'.format(i, j))), 3)
        matrix[j-1][i-1] = round(matrix[i - 1][j - 1] ** (-1), 2)
    a += 1
# Создаём список сумм строки
comp_list = [round(sum(j),2) for j in matrix]
out_list = [round(n/sum(comp_list), 2) for n in comp_list]
if (sum(out_list)) != 1.0:
    index = out_list.index(max(out_list))
    k = (sum(out_list)) - 1.0
    out_list[index] -= k
print('Весовые коэффициенты')
for ind in out_list:
    print(ind, end=' ')
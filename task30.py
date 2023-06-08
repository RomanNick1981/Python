a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
k = int(input('Введите количество элементов: '))
list = []
for n in range(1, k + 1):
    list.append(a1 + d*(n - 1))
print(list)
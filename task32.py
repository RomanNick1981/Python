# k = int(input('Введите количество элементов списка: '))
# list = [int(input()) for i in range(k)]
# min_number = int(input('Введите минимальное значение: '))
# max_number= int(input('Введите максимальное значение: '))
# list_ind = [j for j in range(k) if min_number <= list[j] <= max_number]
# print(list_ind)


# Второй вариант

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print('Дан список: ',list_1)
min_number = int(input('Введите минимальное значение: '))
max_number= int(input('Введите максимальное значение: '))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)
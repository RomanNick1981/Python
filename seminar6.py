# # Задача 39 первая версия
# N = int(input('Введите количество элементов: '))
# list1 = []
# for i in range (N):
#     a = int(input('Введите элемент массива: '))
#     list1.append(a)

# M = int(input('Введите количество элементов: '))
# list2 = []
# for j in range (M):
#     b = int(input('Введите элемент массива: '))
#     list2.append(b)

# new_list = []
# def result(list1, list2):
#     for i in range(N):
#         if list1[i] not in list2:
#             new_list.append(list1[i])
#     return(new_list)

# print(result(list1, list2))

# # Задача 39 первый вариант Преподователя
# from random import randint as rd


# n = int(input())
# list_1 = [rd(1, 11) for i in range(n)]
# print(list_1)
# m = int(input())
# list_2 = [rd(1, 11) for j in range(m)]
# print(list_2)
# for i in list_1:
#     if i not in list_2:
#         print(i, end=' ')
        
# # Задача 39 второй вариант Преподователя
# from random import randint as rd


# n = int(input())
# list_1 = [rd(1, 11) for i in range(n)]
# print(f'---------------------\nСписок 1: {list_1}\n------------------')
# m = int(input())
# list_2 = [rd(1, 11) for j in range(m)]
# print(f'---------------------\nСписок 2: {list_2}\n------------------')
# print('Результат:', [i for i in list_1 if i not in list_2])

# Задание 41
# Решение по С Шарпски

# def result(list):
#     count = 0
#     for i in range(1, len(list1) - 1):
#         if list1[i] > list1[i - 1] and list1[i] > list1[i + 1]:
#             count += 1
#     return(count)

# N = int(input('Введите количество элементов: '))
# list1 = []
# for i in range(N):
#     a = int(input('Введите элемент массива: '))
#     list1.append(a)
# print(list1)
# print(result(list1))

# Задание 41 решение по Питонски 

# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# print(sum([int(list_1[i - 1] < list_1[i] > list_1[i + 1]) for i in range(1, n - 1)]))

# Задача 43 решение через список
# n = int(input('Введите количество элементов: '))
# list = []
# for i in range(n):
#     a = int(input('Введите элемент массива: '))
#     list.append(a)
# print(list)
# def nums(list):
#     count = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if list[i] == list[j]:
#                 count += 1
#     return(count)
# print(nums(list))
# задача 43 решение через словарь

# list_1 = [int(i) for i in input().split()]
# result = {}
# for element in list_1:
#     if element in result:
#         result[element] += 1
#     else:
#         result[element] = 1
# print(sum([i // 2 for i in result.values()]))
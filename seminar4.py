# # task 25 
# string1 = 'a a a b c a a d c d d'
# list1 = string1.split()
# dict1 = {}
# for i in list1:
#     if i in dict1:
#         dict1[i] += 1
#         print(f'{i}_{dict1[i]}', end = ' ')
#     else: 
#         dict1[i] = 0
#         print(i, end = ' ')

# # task25 ver 2
# word = input("Введите текст: ").split()
# result = {}
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else: # ключа i нет внутри словаря result
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# Задание 27
# word = input("Введите текст: ").lower()
# text = word.replace('.', ' ').split()
# text = set(text)
# print(len(text))

# задание 27 Ver 2 Вариант в одну строчку
# print(len(set(input("Введите текст: ").lower().split())))

# Задание 29 Петя и Ваня писали код
n = int(input("Введите число: "))
max_number = n
while n != 0 or n > 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
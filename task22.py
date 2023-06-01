n = int(input('Введите количество чисел первого множества: '))
list1 = []
for i in range(n):
    list1.append(int(input()))
m = int(input('Введите количество чисел второго множества: '))
list2 = []
for j in range(m):
    list2.append(int(input()))
set1 = set(list1)
set2 = set(list2)
res = set1.intersection(set2)
print(res)
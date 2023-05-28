n = int(input('Введите количество элементов: '))
list = [int(input()) for i in range(n)]
x = int(input("Введите искомое число:"))
res = list[0]
for i in list:
    if abs(res - x) > abs(i - x):
        res = i
print("Ответ:",res)
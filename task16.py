n = int(input('Введите количество элементов: '))
list = [int(input()) for i in range(n)]
x = int(input("Введите искомое число:"))
count = 0
for i in list:
    if i == x:
        count +=1
print("Ответ:",count)
print("Петя загадал вам числа, А и Б от 1000")
a = int(input("Вы - Катя, назовите число А "))
b = int(input("Вы - Катя, назовите число Б "))
flag = False
for i in range(a):
    for j in range(b):
        if a == i + j and b == i * j:
            print(i, j)
            flag = True
if not flag:
    print("Петя вас наколол")
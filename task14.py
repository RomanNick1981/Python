print("Ведите натуральное число до которого нужно посчитать степень 2 ки")
try:
    n = int(input())
except:
    n = 0
while n < 1:
    print("Неверный ввод!")
    try:
        n = int(input())
    except:
        n = 0

res = 1
while res <= n:
    print(res)
    res *= 2
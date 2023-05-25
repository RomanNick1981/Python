n = int(input("Введите число: "))
result = 1
i = 2
while i <= n:
    result *= i # result = result * i
    i += 1
print(f'{n}! = {result}')
def summa_numbers(a, b):
    if b == 0:
        return a
    return summa_numbers(a + 1, b - 1)


a = int(input())
b = int(input())
print(summa_numbers(a, b))
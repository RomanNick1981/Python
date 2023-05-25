n = int(input("Введите кол-во дней: "))
count = 0
max_count_days = 0
for i in range(n):
    x = int(input("Введите среднюю температуру дня: "))
    if x > 0:
        count += 1
    else:
        count = 0

    if max_count_days < count:
        max_count_days = count
print(max_count_days)
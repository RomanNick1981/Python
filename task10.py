n = 0
while n < 1:
    try:
        n = int(input()) 
    except:
        print("Введите натуральное число!")
        n = 0

count_zero = 0
count_one = 0
i = 0
while i < n:
    try:
        x = int(input())
    except:
        print("Введите 1 или 0!")
        continue

    if x == 0:
        count_zero += 1
    elif x == 1:
        count_one += 1
    else:
        print("Введите 1 или 0!")
        continue
    i += 1
        
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
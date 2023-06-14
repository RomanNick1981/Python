text = input().lower().split()
result = set() 
vowels = 'ёеаоэяиюуы' # Строка гласных можно без запятых
for word in text:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    result.add(count)
if len(result) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
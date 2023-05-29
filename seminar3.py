# n = int (input("Введите количесво элементов: "))
# i = 0
# list = [int(input("Введите элемент: ")) for item in range(n)]
# list1  =  set(list)
# print(len(list1))

# data = [int(i) for i in input("Введите числа: ").split()]
# step = int(input("Введите кол-во сдвигов: "))
# step = step % len(data)
# data = [data[i - step] for i in range(len(data))]
# print(data)

# data = [[10, 15], [53, 35, 84]]
# print(data[0][1], [1, 2])

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#            {"VIII":"S007"}]
# result = set()
# for item in data:
#     for key in item:
#         result.add(item[key])
# print(*result)

# data = {'Ivan': 21, "Alexandr": 35, 'Mariy': 27}
# print(list(data.values()))
# print(list(data.keys()))

# array = int(input('Введите количество элементов: '))
# list = [int(input("Введите элемент массива: ")) for item in range(array)]
# count = 0 
# for i in range(len(list) - 1):
#     if list[i] < list[i + 1]:
#         count += 1
# print(count)


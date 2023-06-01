n = int(input())
array = [int(i) for i in input().split()][:n]
max_summa = 0
for i in range(1, len(array) - 1):
   if max_summa < array[i - 1] + array[i] + array[i + 1]:
      max_summa = array[i - 1] + array[i] + array[i + 1]

if max_summa < array[0] + array[1] + array[len(array) - 1]:
   max_summa = array[0] + array[1] + array[len(array) - 1]
if max_summa < array[0] + array[len(array) - 1] + array[len(array) - 2]:
   max_summa = array[0] + array[len(array) - 1] + array[len(array) - 2]
print(max_summa)
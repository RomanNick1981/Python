s = int(input())
s1, s2 = s % 1000,s // 1000
sum1 = s1 // 100 + s1//10 % 10 + s1 % 10
sum2 = s2 // 100 + s2//10 % 10 + s2 % 10
if sum1 == sum2:
    print("yes")
else:
    print("no")
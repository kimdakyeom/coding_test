n = int(input())
num = list(map(int,input().split(" ")))
min = num[0]
max = num[0]

for i in range(n):
    if (num[i] < min):
        min = num[i]
    if (num[i] > max):
        max = num[i]
print(min, max)
n = int(input())
a = input().split(" ")
list = []

for i in range(0, n):
    a[i] = int(a[i])

for i in range(24):
    list.append(0)

for i in range(n):
    list[a[i]] += 1

for i in range(1, 24):
    print(list[i], end=' ')
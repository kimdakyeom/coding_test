n = int(input())
num = input().split(" ")
list = []

for i in range(n):
    num[i] = int(num[i])

for i in range(-10000, 10000):
    list.append(0)

for i in range(n):
    list[num[i]] += 1

for i in range(-10000, 10000):
    if list[i] > 0:
        print(i)
        break
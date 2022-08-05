n, x = map(int, input().split(" "))
num = map(int, input().split(" "))

list = list(num)

for i in range(0, n):
    if(list[i] < x):
        print(list[i], end=' ')
    else:
        continue
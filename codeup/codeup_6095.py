n = int(input())
list = [[0] *19 for i in range(19)]

for i in range(n):
    x, y = map(int, input().split(" "))
    list[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(list[i][j], end=' ')
    print() # 줄 한칸 띄우기
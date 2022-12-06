def division(x, y, n):
    global cnt_0, cnt_1
    color = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                division(x, y, n//2)
                division(x+n//2, y, n//2)
                division(x, y+n//2, n//2)
                division(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

cnt_0, cnt_1 = 0, 0
division(0, 0, n)
print(cnt_0)
print(cnt_1)
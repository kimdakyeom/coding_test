import sys
sys.stdin = open("swea_1210_input.txt", 'rt', encoding='UTF8')

arr = [list(map(int, input().split())) for _ in range(10)]

dx = [1, -1, 0]
dy = [0, 0, -1]

x = arr[9].index(2)
y = 9
k = 0

while y > 0:
    nx = x + dx[k]
    ny = y + dy[k]

    if 0 <= nx < 10 and 0 <= ny < 10 and arr[ny][nx]:
        arr[ny][nx] = 0
        x = nx
        y = ny
        k = 0

    else:
        k = (k+1) % 3
print(x)
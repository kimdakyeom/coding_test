c, r = map(int, input().split())
seat = int(input())

if seat > c * r:
    print(0)

arr = [[0] * c for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y, dir = 0, 0, 0

for i in range(1, r * c + 1):
    if i == seat:
        print(y + 1, x + 1)
        break
    else:
        arr[x][y] = i
        x += dx[dir]
        y += dy[dir]

        if x < 0 or y < 0 or x >= r or y >= c or arr[x][y]:
            x -= dx[dir]
            y -= dy[dir]
            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
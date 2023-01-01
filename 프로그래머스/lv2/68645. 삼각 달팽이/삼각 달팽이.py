def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    dirs = [(1,0), (0,1), (-1,-1)]
    all = n * n
    for i in range(1, n):
        all -= i
    x, y = 0, 0
    i = 1
    dir = 0
    while i <= all:
        arr[y][x] = i
        dy, dx = dirs[dir]
        ny = y + dy
        nx = x + dx
        i += 1
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
            y, x = ny, nx
        else:
            dir = (dir + 1) % 3
            dy, dx = dirs[dir]
            y += dy
            x += dx
    for row in arr:
        for i in row:
            answer.append(i)
    return answer
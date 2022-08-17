n = int(input())

paper = [[0] * 1001 for _ in range(1001)]

for k in range(1, n + 1):
    x, y, p, q = map(int, input().split())
    for i in range(x, x + p):
        for j in range(y, y + q):
            paper[i][j] = k

cnt = [0] * (n + 1)

for i in range(1001):
    for j in range(1001):
        if paper[i][j]:
            cnt[paper[i][j]] += 1

for i in range(1, n + 1):
    print(cnt[i])
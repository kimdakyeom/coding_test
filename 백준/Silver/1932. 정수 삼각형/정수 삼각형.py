import sys
input = sys.stdin.readline
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

len = 2
for i in range(1, n):
    for j in range(len):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif i == j:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])
    len += 1
print(max(tri[n-1]))
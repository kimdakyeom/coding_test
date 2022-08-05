import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for tc in range(k):
    i, j, x, y = map(int, input().split())
    sum = 0

    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += matrix[a][b]
    print(sum)
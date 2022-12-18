import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
n, m = map(int, input().split())

def sum_table(a):
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            table[i][j] = (table[i][j-1] + table[i-1][j] - table[i-1][j-1]) + a[i-1][j-1]
    return table

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

t = sum_table(arr)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(t[x2][y2] - t[x2][y1-1] - t[x1-1][y2] + t[x1-1][y1-1])
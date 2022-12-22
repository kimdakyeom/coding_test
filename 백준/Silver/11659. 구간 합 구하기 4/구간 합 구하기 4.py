import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
n, m = map(int, input().split())

def sum_table(a):
    table = [0] * (n+1)
    for i in range(1, n+1):
        table[i] = table[i-1] + a[i-1]
    return table

nums = list(map(int, input().split()))

t = sum_table(nums)
# print(t)
for _ in range(m):
    i, j = map(int, input().split())
    print(t[j]-t[i-1])
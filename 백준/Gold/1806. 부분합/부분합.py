import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
n, s = map(int, input().split())

def sum_table(a):
    table = [0] * (n+1)
    for i in range(1, n+1):
        table[i] = table[i-1] + a[i-1]
    return table

nums = list(map(int, input().split()))
t = sum_table(nums)

answer = 1e8
start = 0
end = 1

while start != n:
    if t[end] - t[start] >= s:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

if answer == 1e8:
    print(0)
else:
    print(answer)
import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
n, h= map(int,input().split())
up = [0] * (h+1)
down = [0] * (h+1)

for i in range(n):
    if i % 2 == 1:
        up[int(input())] += 1
    else:
        down[int(input())] += 1

for i in range(h-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

for i in range(1, h+1):
    up[h-i+1] += down[i]

min_h = min(up[1:])
print(min_h, end=' ')

answer = 0
for i in range(1, h+1):
    if up[i] == min_h:
        answer += 1
print(answer)
import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, d):
    oven[i] = min(oven[i], oven[i-1])

answer = 0
cnt = 0
idx = d-1
for p in pizza:
    while idx >= 0:
        if p <= oven[idx]:
            answer = idx
            idx -= 1
            cnt += 1
            break
        else:
            idx -= 1

if cnt == len(pizza):
    print(answer+1)
else:
    print(answer)
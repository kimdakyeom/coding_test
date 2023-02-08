import sys
input = sys.stdin.readline


def back(depth):
    global ans
    if len(answer) > 0:
        sour = 1
        bitter = 0
        for a in answer:
            sour *= a[0]
            bitter += a[1]
        if ans > abs(sour - bitter):
            ans = abs(sour - bitter)
    for i in range(depth, n):
        answer.append((gre[i][0], gre[i][1]))
        back(i+1)
        answer.pop()

ans = 1e9
n = int(input())
gre = []
for _ in range(n):
    s, b = map(int, input().split())
    gre.append((s, b))
answer = []
back(0)
print(ans)
import sys
input = sys.stdin.readline

n = int(input())

def solve(k):
    c = {}
    for i in range(k):
        name, cat = input().split()
        if cat not in c:
            c[cat] = 2
        else:
            c[cat] += 1
    answer = 1
    for value in c.values():
        answer *= value
    print(answer-1)

for _ in range(n):
    k = int(input())
    solve(k)
import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
answer = [0 for _ in range(n)]
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, top[i]))
print(*answer)
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
stack = list()
answer = [-1 for _ in range(n)]

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
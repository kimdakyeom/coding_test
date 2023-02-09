import sys
input = sys.stdin.readline

def back(depth):
    global cnt
    if answer and sum(answer) == s:
        cnt += 1
    for i in range(depth, n):
        answer.append(arr[i])
        back(i+1)
        answer.pop()

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
cnt = 0
back(0)
print(cnt)
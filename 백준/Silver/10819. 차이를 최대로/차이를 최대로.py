import sys
input = sys.stdin.readline


def back(depth):
    global ans
    if depth == n:
        total = 0
        for i in range(1, n):
            total += abs(answer[i-1] - answer[i])
        ans = max(ans, total)
        return ans
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer.append(a[i])
            back(depth+1)
            visited[i] = 0
            answer.pop()


n = int(input())
a = list(map(int, input().split()))
visited = [0] * n
answer = []
ans = 0
back(0)
print(ans)
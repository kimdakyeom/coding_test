import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
liter = list(map(int, input().split()))
min_liter = liter[0]
# 제일 작은 거랑 비교해서 제일 작으면 갱신 * 제일 작은 거
answer = dis[0] * liter[0]

for i in range(1, n-1):
    if min_liter > liter[i]:
        min_liter = liter[i]
    answer += dis[i] * min_liter

print(answer)
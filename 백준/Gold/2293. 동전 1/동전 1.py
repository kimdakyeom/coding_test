import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

dp = [0 for i in range(k+1)]
dp[0] = 1

for i in money:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])
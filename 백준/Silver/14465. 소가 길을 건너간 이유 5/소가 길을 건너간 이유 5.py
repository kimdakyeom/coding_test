import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
broke = []
for i in range(b):
    broke.append(int(input()))
answer = [0] * (n - k + 1)
arr = [1] * (n+1)
for b in broke:
    arr[b] = 0
sum_ = sum(arr[1:k+1])
min_ = k - sum_
for i in range(2, n-k+2):
    sum_ = sum_ - arr[i-1] + arr[i+k-1]
    min_ = min(min_, k - sum_)
print(min_)
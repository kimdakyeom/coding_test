import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum_v = 0
answer = 0
dic = {0:1}

for a in arr:
    sum_v += a
    if sum_v - k in dic:
        answer += dic[sum_v - k]
    if sum_v not in dic:
        dic[sum_v] = 1
    else:
        dic[sum_v] += 1
print(answer)
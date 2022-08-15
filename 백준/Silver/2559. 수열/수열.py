n, k = map(int, input().split())
temp = list(map(int, input().split()))

ans = []
ans = [sum(temp[:k])]

for i in range(0, len(temp) - k):
    ans.append(ans[-1] - temp[i] + temp[i+k])
print(max(ans))
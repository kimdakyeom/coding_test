n = int(input())

sequence = list(map(int, input().split()))
prev = sequence[0]
min_cnt, max_cnt = 1, 1
ans = 1

for i in range(1, len(sequence)):
    if sequence[i] >= prev:
        min_cnt += 1
    else:
        min_cnt = 1
    if sequence[i] <= prev:
        max_cnt += 1
    else:
        max_cnt = 1
    prev = sequence[i]
    ans = max(ans, min_cnt, max_cnt)
print(ans)
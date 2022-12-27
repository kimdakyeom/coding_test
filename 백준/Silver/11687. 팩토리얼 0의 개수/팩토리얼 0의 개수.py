from math import factorial

def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

m = int(input())

start, end, answer = 1, m*5, 0

while start <= end:
    mid = (start + end) // 2
    cnt = five_count(mid)
    if cnt < m:
        start = mid + 1
    elif cnt > m:
        end = mid - 1
    else:
        end = mid - 1
        answer = mid
if answer:
    print(answer)
else:
    print(-1)
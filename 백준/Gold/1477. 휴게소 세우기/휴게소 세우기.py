import sys
input = sys.stdin.readline
import math

n, m, l = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(l)
rest.sort()

start, end = 1, l-1
answer = 0

while start <= end:
	cnt = 0
	mid = (start + end) // 2
	for i in range(1, len(rest)):
		if rest[i] - rest[i-1] > mid:
			cnt += (rest[i] - rest[i-1] - 1) // mid
	if cnt > m:
		start = mid + 1
	else:
		end = mid - 1
		answer = mid
print(answer)
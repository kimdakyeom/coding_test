import sys
from pprint import pprint
input = sys.stdin.readline

n, c = map(int, input().split())

cnt = 0
house = []

for i in range(n):
    house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]
answer = 0

if c == 2:
    answer = house[-1] - house[0]
else:
    while start < end:
        mid = (start + end) // 2
        now = house[0]
        cnt = 1

        for i in range(1, len(house)):
            if house[i] >= now + mid:
                cnt += 1
                now = house[i]
        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid

print(answer)
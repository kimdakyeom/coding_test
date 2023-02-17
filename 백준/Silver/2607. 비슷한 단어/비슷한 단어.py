import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

n = int(input())
a1 = [0] * 27

first = input().strip()
for k in first:
    a1[ord(k)-64] += 1

answer = 0
for i in range(n-1):
    a2 = [0] * 27
    second = input().strip()
    for k in second:
        a2[ord(k)-64] += 1
    a1_cnt, a2_cnt = 0, 0
    for k in range(27):
        if a1[k] > a2[k]:
            a1_cnt += a1[k] - a2[k]
        if a1[k] < a2[k]:
            a2_cnt += a2[k] - a1[k]
    if a1_cnt <= 1 and a2_cnt <= 1:
        answer += 1
print(answer)

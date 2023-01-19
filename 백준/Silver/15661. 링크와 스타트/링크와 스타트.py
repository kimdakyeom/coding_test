from itertools import combinations
import sys

input = sys.stdin.readline
member = []
n = int(input())
for i in range(n):
    member.append(i)
ans = 1e8
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

for x in range(1, (n//2)+1):
    com = combinations(member, x)
    min_val = 1e9

    for m in com:
        start = list(m)
        link = list(set(member)-set(start))
        start_ans, link_ans = 0, 0
        for i in range(n-1):
            for j in range(n-1):
                try:
                    start_sum = score[start[i]][start[j]]
                except IndexError:
                    start_sum = 0
                try:
                    link_sum = score[link[i]][link[j]]
                except IndexError:
                    link_sum = 0
                start_ans += start_sum
                link_ans += link_sum
        diff = abs(start_ans - link_ans)
        min_val = min(min_val, diff)
    ans = min(ans, min_val)
print(ans)
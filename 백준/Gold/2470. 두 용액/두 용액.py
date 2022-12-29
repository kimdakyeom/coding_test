import sys

input = sys.stdin.readline

n = int(input())

dis = list(map(int, input().split()))
dis.sort()
start = 0
end = len(dis) - 1
answer = abs(dis[start]+dis[end])
answer_list = [dis[start], dis[end]]

while start < end:
    d_start = dis[start]
    d_end = dis[end]

    total = d_start + d_end

    if abs(total) < answer:
        answer = abs(total)
        answer_list = [d_start, d_end]
    if total < 0:
        start += 1
    else:
        end -= 1
print(answer_list[0], answer_list[1])
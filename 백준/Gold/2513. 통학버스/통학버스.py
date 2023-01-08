from heapq import heappush, heappop

def sol(v):
    global answer
    tmp = 0
    distance = 0
    while v:
        pos, num = heappop(v)
        if not distance:
            distance = -pos * 2
            answer += distance
        if tmp + num > k:
            num -= k - tmp
            tmp = 0
            distance = 0
            heappush(v, (pos, num))
        else:
            tmp += num
    return answer

n, k, s = map(int, input().split())
inp = [tuple(map(int, input().split())) for _ in range(n)]
left = []
right = []
for i in inp:
    if i[0] < s:
        heappush(left, (-(s-i[0]), i[1]))
    else:
        heappush(right, (-(i[0]-s), i[1]))

answer = 0

sol(left)
print(sol(right))
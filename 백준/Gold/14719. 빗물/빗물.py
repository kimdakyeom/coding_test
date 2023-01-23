import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

answer = 0
for i in range(1, len(block)):
    mleft = max(block[:i])
    mright = max(block[i:])
    m = min(mleft, mright)
    if block[i] < m:
        answer += m - block[i]
print(answer)
import sys
input = sys.stdin.readline

n = int(input())
line = [0] * n
input_ = list(map(int, input().split()))

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == input_[i] and line[j] == 0:
            line[j] = i + 1
            break
        elif line[j] == 0:
            cnt += 1
print(*line, end=' ')
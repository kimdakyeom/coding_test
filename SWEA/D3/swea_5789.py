# import sys

# sys.stdin = open("swea_5789_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    list_ = [0] * n

    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            list_[j] = i
    print(f'#{tc}', end=' ')
    print(*list_)
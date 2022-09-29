# import sys

# sys.stdin = open("swea_10580_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    list_ = []
    cnt = 0
    for _ in range(n):
        a, b = map(int, input().split())
        list_.append((a, b))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if list_[i][0] < list_[j][0] and list_[i][1] > list_[j][1]:
                cnt += 1
            elif list_[i][0] > list_[j][0] and list_[i][1] < list_[j][1]:
                cnt += 1
    print(f"#{tc} {cnt}")

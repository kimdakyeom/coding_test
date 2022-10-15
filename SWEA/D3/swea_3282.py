# import sys

# sys.stdin = open("swea_3282_input.txt", "rt", encoding="UTF8")


def knapsack(k, n):
    list_ = [[0 for x in range(k + 2)] for x in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # 배낭에 안들어가면
            if v_list[i - 1] > j:
                # 짐이 추가되기 전 가격
                list_[i][j] = list_[i - 1][j]
            # 배낭에 들어가면
            else:
                # 새로 추가된 짐의 가격 + 짐이 추가되기 전, 배낭 용량이 (현재 배낭 용량-새로 추가된 짐 무게)의 값
                # 짐이 추가되기 전 가격
                list_[i][j] = max(w_list[i - 1] + list_[i - 1][j - v_list[i - 1]], list_[i - 1][j])
    return list_[n][k]


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    w_list = []
    v_list = []
    for _ in range(n):
        v, c = map(int, input().split())
        v_list.append(v)
        w_list.append(c)
    print(f"#{tc} {knapsack(k, n)}")

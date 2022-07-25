# import sys
# sys.stdin = open("swea_1208_input.txt", "r")

T = 10

for t in range(1, T+1):
    dump = int(input())
    floor = list(map(int, input().split()))

    for i in range(dump):
        # floor에서 가장 큰 값
        max_ = max(floor)
        # floor에서 가장 작은 값
        min_ = min(floor)

        # floor for문으로 순회
        for j in range(len(floor)):
            # 만약 floor가 max이면
            if floor[j] == max_:
                # floor에 1 빼기
                floor[j] -= 1
                # 그만
                break
        # floor for문으로 순회
        for k in range(len(floor)):
            # 만약 floor가 min이면
            if floor[k] == min_:
                # floor에 1 더하기
                floor[k] += 1
                # 그만
                break

    # max에서 min 빼기
    print(f'#{t} {max(floor) - min(floor)}')
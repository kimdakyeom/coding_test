# import sys
# sys.stdin = open("swea_1206_input.txt", "r")

T = 10

for t in range(1, T+1):
    building = int(input())
    floor = list(map(int, input().split()))

    sum = 0

    for i in range(2, building-2):
        minus = []

        if floor[i-2] < floor[i] and floor[i-1] < floor[i] and floor[i+1] < floor[i] and floor[i+2] < floor[i]:
            minus.append(floor[i] - floor[i-2])
            minus.append(floor[i] - floor[i-1])
            minus.append(floor[i] - floor[i+1])
            minus.append(floor[i] - floor[i+2])

            min_ = min(minus)
            sum += min_
    print(f'#{t} {sum}')
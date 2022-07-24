# import sys
# sys.stdin = open("swea_13229_input.txt", "r")

T = int(input())

day = ["SAT", "FRI", "THU", "WED", "TUE", "MON", "SUN"]
for t in range(1, T+1):
    s = input()

    for i in range(len(day)):
        if s == day[i]:
            print(f'#{t} {i+1}')
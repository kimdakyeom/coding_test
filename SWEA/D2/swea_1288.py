# import sys
# sys.stdin = open("swea_1288_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    N = int(input())
    list = [0] * 10
    mul = 0

    while True:
        if 0 not in list:
            break
        else:
            mul += 1
            num = str(N*mul)
            for j in range(len(num)):
                list[int(num[j])] = 1
    print(f'#{i} {num}')
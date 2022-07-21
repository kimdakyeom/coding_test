# import sys
# sys.stdin = open("swea_1984_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    num = list(map(int, input().split()))

    sum = 0
    avg = 0

    num.remove(max(num))
    num.remove(min(num))

    for i in num:
        sum += i
        avg = round(sum / len(num))

    print(f'#{T} {avg}')
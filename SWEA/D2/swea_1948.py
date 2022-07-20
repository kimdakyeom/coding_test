# import sys
# sys.stdin = open("swea_1948_input.txt", "r")

n = int(input())

cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, n+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0
    if m1 == m2:
        ans = d2 - d1 + 1
    else:
        for j in range(m1, m2):
            ans += cal[j-1]
        ans = ans + d2 - d1 + 1
    print(f'#{i} {ans}')
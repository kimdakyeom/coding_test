# import sys
# sys.stdin = open("swea_12741_input.txt", "r")

T = int(input())
list = []

for t in range(1, T+1):
    a, b, c, d = map(int, input().split())
    
    if b < c or d < a:
        ans = 0
    else:
        ans = min(b,d) - max(a, c)
    list.append(f'#{t} {ans}')

for l in list:
    print(l)
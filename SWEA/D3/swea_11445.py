import sys
sys.stdin = open("swea_11445_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    p = input()
    q = input()

    if q == p + 'a':
        print(f'#{t} N')
    else:
        print(f'#{t} Y')
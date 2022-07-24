# import sys
# sys.stdin = open("swea_12004_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    cnt = 0
    list = []

    for i in range(1, 10):
        if n % i == 0 and len(str(n // i)) == 1:
            list.append(i)
            list.append(n//i)
    
    if len(list) == 0:
        print(f'#{t} No')
    else:
        print(f'#{t} Yes')
# import sys
# sys.stdin = open("swea_11736_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    
    for i in range(1, n-1):
        # 두번째 숫자가 첫번째 숫자와 세번째 숫자 사이에 있다면
        if num[i-1] < num[i] < num[i+1] or num[i-1] > num[i] > num[i+1]:
            # 1씩 더하기
            cnt += 1

    print(f'#{t} {cnt}')
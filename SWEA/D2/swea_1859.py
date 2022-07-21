# import sys
# sys.stdin = open("swea_1859_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    # num의 마지막 값을 최대값으로 지정
    max = num[-1]
    # 이익 변수 초기화
    profit = 0

    # n-2 인덱스부터 0 인덱스까지 1씩 감소하면서 반복
    for i in range(n-2, -1, -1):
        # 만약 현재 값이 max보다 크면
        if num[i] >= max:
            # max는 현재 값으로 변경
            max = num[i]
        # 현재 값이 max보다 크지 않으면
        else:
            # max와 현재값의 차익을 profit 변수에 더함
            profit += max - num[i]
    
    print(f'#{T} {profit}')

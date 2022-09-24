# import sys
# sys.stdin = open("swea_11445_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    # 입력값에 공백이 있으므로 공백 제거
    p = input().rstrip()
    q = input().rstrip()

    # p에 'a'를 붙인 값이 q와 일치하지 않다면
    # p와 q 사이에 다른 단어가 있는 것
    if p + 'a' != q:
        print(f'#{t} Y')
    else:
        print(f'#{t} N')
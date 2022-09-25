# import sys
# sys.stdin = open("swea_10965_input.txt", "r", encoding='UTF-8')

# 2부터 3162까지의 소수를 담은 리스트 만들기
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: 
            break
    else:
        prime.append(i)

ans_list = []
T = int(input())
# 소수에 대해서만 a가 나누어떨어지는지 확인
for tc in range(1, T + 1):
    a = int(input())
    # a에 곱한 결과가 거듭제곱수가 되는 최소의 자연수
    b = 1
    # a가 제곱근이 아니면
    if a ** 0.5 != int(a ** 0.5):
        # prime에 있는 소수값에 접근
        for p in prime:
            cnt = 0
            # a가 p로 나눠지지 않으면
            while not a % p:
                # a를 p로 나눈 후
                a //= p
                # 개수 증가
                cnt += 1
            # cnt가 홀수이면
            if cnt % 2:
                # 해당 소수 곱하기
                b *= p
            # a가 1이거나 a가 소수보다 작으면
            if a == 1 or p > a:
                # 시간을 줄이기 위해 break
                break
        # 모든 소수로 나눠지지 않는다면
        # 해당 값은 prime의 최대값보다 더 큰 소수값이므로
        if a > 1:
            # b에 해당 값을 곱하기
            b *= a
    ans_list.append('#{} {}'.format(tc, b))

for ans in ans_list:
    print(ans)
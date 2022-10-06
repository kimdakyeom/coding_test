# import sys

# sys.stdin = open("swea_5986_input.txt", "rt", encoding="UTF8")

# 2-1000 중 소수만 리스트에 넣어놓기
prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

for tc in range(1, int(input()) + 1):
    n = int(input())
    cnt = 0
    # 소수 리스트 순회
    # 첫번째 값이 n보다 크면 탈출
    for i in range(len(prime)):
        if prime[i] > n:
            break
        # 두번째 값이 n보다 크면 탈출
        for j in range(i, len(prime)):
            if prime[j] > n:
                break
            # 세번째 값이 n보다 크면 탈출
            for k in range(j, len(prime)):
                if prime[k] > n:
                    break
                
                # 세 값을 다 더한게 n이면
                if prime[i] + prime[j] + prime[k] == n:
                    # 횟수 증가
                    cnt += 1
    print(f'#{tc} {cnt}')
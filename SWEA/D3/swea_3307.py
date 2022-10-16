# import sys

# sys.stdin = open("swea_3307_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    # DP 테이블 생성
    dp = [1] * n

    # 수열의 2번째 값부터 하나씩 확인
    for i in range(1, n):
        for j in range(0, i):
            # 직전 값보다 크면 i번째 값을 업데이트
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    answer = max(dp)
    print(f"#{tc} {answer}")

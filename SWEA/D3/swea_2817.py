import sys
sys.stdin = open("swea_2817_input.txt", "r")

def solve(i, sum):
    global answer
    # n번까지만 반복
    if i >= n:
        return
    # 여태까지 모든 합 + 현재 값
    temp = sum + a[i]
    # 합이 k면
    if temp == k:
        answer += 1

    # 현재 인덱스의 값을 더하지 않았을 때
    solve(i + 1, sum)
    # 현재 인덱스의 값을 더했을 때
    solve(i + 1, temp)
    
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    answer = 0
    solve(0, 0)
    print(f'#{tc} {answer}')
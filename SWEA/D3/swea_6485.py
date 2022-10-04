# import sys

# sys.stdin = open("swea_6485_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    # 처음에 리스트로 했다가 런타임에러 나서 딕셔너리로
    stop = {}

    # 5000개의 딕셔너리에 값 0 넣기
    for i in range(1, 5001):
        stop[i] = 0

    answer = []
    for i in range(n):
        a, b = map(int, input().split())
        # a 이상 b 이하동안
        for k in range(a, b + 1):
            # 나오는 값 1씩 더해주기
            stop[k] += 1
    p = int(input())
    for i in range(p):
        # answer 리스트에 딕셔너리의 input 인덱스를 넣기
        answer.append(stop[int(input())])
    print(f"#{tc}", end=" ")
    print(*answer)

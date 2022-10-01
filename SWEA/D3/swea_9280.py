# import sys

# sys.stdin = open("swea_9280_input.txt", "rt", encoding="UTF8")

from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    r = []
    w = []
    use = [0] * n
    answer = 0
    wait = deque()

    for _ in range(n):
        r.append(int(input()))
    for _ in range(m):
        w.append(int(input()))

    for _ in range(m * 2):
        i = int(input())
        # 들어오는 차면
        if i > 0:
            # 만약 비어있는 자리가 있으면
            if 0 in use:
                # n번 반복
                for k in range(n):
                    # 비어있는 자리에
                    if use[k] == 0:
                        # i 차 넣기
                        use[k] = i
                        break
            # 비어있는 자리가 없으면
            else:
                # wait 큐에 차 넣기
                wait.append(i)
        # 나가는 차면
        else:
            # 주차장에서 index 찾기
            out = use.index(-i)
            # 자리 비우기
            use[out] = 0
            # 해당 차의 무게 * 책정된 단위 무게당 금액
            answer += w[-i - 1] * r[out]
            # 기다리고 있는 차가 있으면
            if wait:
                # 빠져나간 자리에 해당 차 넣기
                use[out] = wait.popleft()
    print(f"#{tc} {answer}")

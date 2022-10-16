import sys

# sys.stdin = open("swea_3499_input.txt", "rt", encoding="UTF8")
from collections import deque

for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = []
    list_ = list(map(str, input().split()))
    # 길이가 짝수면
    if n % 2 == 0:
        # 앞 반 뒤 반 나눠서 덱에 넣기
        deque1 = deque(list_[: n // 2])
        deque2 = deque(list_[n // 2 :])
    # 길이가 홀수면
    else:
        # 앞 반의 반올림, 뒤 나머지 덱에 넣기
        deque1 = deque(list_[: n // 2 + 1])
        deque2 = deque(list_[n // 2 + 1 :])
    # answer의 인덱스 판단
    for i in range(n):
        if i % 2 == 0:
            # 짝수 인덱스에는 deque1 값 넣기
            answer.append(deque1.popleft())
        else:
            answer.append(deque2.popleft())

    print(f"#{tc}", end=" ")
    print(*answer, end=" ")
    print()

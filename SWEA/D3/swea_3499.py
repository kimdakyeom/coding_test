import sys

sys.stdin = open("swea_3499_input.txt", "rt", encoding="UTF8")
from collections import deque

for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = []
    list_ = list(map(str, input().split()))
    if n % 2 == 0:
        deque1 = deque(list_[: n // 2])
        deque2 = deque(list_[n // 2 :])
    else:
        deque1 = deque(list_[: n // 2 + 1])
        deque2 = deque(list_[n // 2 + 1 :])
    while len(deque1) != 0 and len(deque2) != 0:
        answer.append(deque1.popleft())
        answer.append(deque2.popleft())
        # to be continue...
    print(answer)

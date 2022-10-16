# import sys

# sys.stdin = open("swea_3314_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    scores = list(map(int, input().split()))
    for i in range(len(scores)):
        if scores[i] < 40:
            scores[i] = 40
    print(f"#{tc} {sum(scores) // len(scores)}")

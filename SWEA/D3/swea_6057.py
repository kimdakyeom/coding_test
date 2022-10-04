import sys

sys.stdin = open("swea_6057_input.txt", "rt", encoding="UTF8")

from collections import defaultdict

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    # 딕셔너리에 디폴트 값을 list로 주기
    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        # 해당 정점과 이어진 정점을 리스트 형태로 추가
        graph[x].append(y)
        graph[y].append(x)

    answer = 0
    # 삼각형을 이루고 있다면
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i in graph[j] and j in graph[k] and k in graph[i]:
                    answer += 1
    print(f"#{tc} {answer}")

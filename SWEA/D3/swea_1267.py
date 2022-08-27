import sys
sys.stdin = open("swea_1267_input2.txt", 'rt', encoding='UTF8')

for t in range(1, 2):
    v, e = map(int, input().split())
    graph = [[0] * (v+1) for _ in range(v+1)]

    data = list(map(int, input().split()))
    n = int(len(data) / 2)

    for i in range(n):
        row = data[i * 2]
        col = data[i * 2 + 1]
        graph[col][row] = 1

    visited = []
    while True:
        if len(visited) == v:
            break
        start_col = []
        for col in range(1, len(graph)):
            if 1 not in graph[col] and col not in visited:
                start_col.append(col)
        for col in start_col:
            visited.append(col)
            for row in range(len(graph)):
                graph[row][col] = 0

    print(f'#{t}', end=' ')
    for i in visited:
        print(f'{i}', end=' ')
    print()
n = int(input())
m = int(input())

# 경로 저장하기 위한 2차원 리스트
graph = [[] for _ in range(n+1)]

# 경로를 graph에 저장
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 답 변수 초기화
cnt = 0
# 다녀간 정점 확인 위한 변수
visited = [0] * (n+1)

def dfs(start):
    global cnt
    # 인덱스1에 1 저장
    visited[start] = 1
    # 그래프 탐색
    for i in graph[start]:
        # 다녀가지 않았으면
        if visited[i] == 0:
            # dfs함수를 그 수부터 탐색
            dfs(i)
            # 답에 1 더하기
            cnt += 1

# 1부터 탐색
dfs(1)
print(cnt)
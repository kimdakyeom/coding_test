n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]

row = []
col = []

# 가로 순회
for i in range(n):
    # 가로 문자열에 X의 유무 row에 저장
    row.append("X" not in matrix[i])

# 세로 순회
for j in range(m):
    # 세로 문자열에 X의 유무 col에 저장
    col.append("X" not in [matrix[i][j] for i in range(n)])

# 최소이므로 겹치는건 가로와 세로에 모두 있기때문에
# 가로의 합과 세로의 합 중 더 큰 값 출력
print(max(sum(row), sum(col)))
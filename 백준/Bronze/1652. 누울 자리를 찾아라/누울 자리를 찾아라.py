n = int(input())
matrix = []
cnt_list = []

transposed_matrix = [[0] * n for _ in range(n)]
transposed_cnt_list = []

for tc in range(n):
    room = list(input())
    matrix.append(room)

for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[i][j] == ".":
            cnt += 1
            cnt_list.append(cnt)
        if matrix[i][j] == "X":
            cnt = 0
print(cnt_list.count(2), end=' ')

for i in range(n):
    for j in range(n):
        transposed_matrix[i][j] = matrix[j][i]

for i in range(n):
    cnt = 0
    for j in range(n):
        if transposed_matrix[i][j] == ".":
            cnt += 1
            transposed_cnt_list.append(cnt)
        if transposed_matrix[i][j] == "X":
            cnt = 0
print(transposed_cnt_list.count(2))
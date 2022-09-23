def rotate(queries, arr):
    x1, y1, x2, y2 = queries
    mins = []
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    for i in range(y2 - 1, y1 - 1, -1):
        arr[x1][i], arr[x1][i + 1] = arr[x1][i + 1], arr[x1][i]
        mins.append(arr[x1][i])
        mins.append(arr[x1][i + 1])
    for i in range(x1, x2):
        arr[i][y1], arr[i + 1][y1] = arr[i + 1][y1], arr[i][y1]
        mins.append(arr[i][y1])
        mins.append(arr[i + 1][y1])
    for i in range(y1, y2):
        arr[x2][i], arr[x2][i + 1] = arr[x2][i + 1], arr[x2][i]
        mins.append(arr[x2][i])
        mins.append(arr[x2][i + 1])
    for i in range(x2 -1, x1, -1):
        arr[i][y2], arr[i + 1][y2] = arr[i + 1][y2], arr[i][y2]
        mins.append(arr[i][y2])
        mins.append(arr[i + 1][y2])
    mins = set(mins)
    return (arr, min(mins))

def solution(rows, columns, queries):
    answer = []

    arr = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = (i * columns + j + 1)
    
    for q in queries:
        arr, min_ = rotate(q, arr)
        answer.append(min_)
    return answer
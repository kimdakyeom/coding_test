def solution(rows, columns, queries):
    answer = []
    arr = [[0 for col in range(columns+1)] for row in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for col in range(1, columns+1):
            arr[row][col] = num
            num += 1
    for x1, y1, x2, y2 in queries:
        tmp = arr[x1][y1]
        mini = tmp

        for k in range(x1, x2):
            test = arr[k+1][y1]
            arr[k][y1] = test
            mini = min(mini, test)
        for k in range(y1, y2):
            test = arr[x2][k+1]
            arr[x2][k] = test
            mini = min(mini, test)
        for k in range(x2, x1, -1):
            test = arr[k-1][y2]
            arr[k][y2] = test
            mini = min(mini, test)
        for k in range(y2, y1, -1):
            test = arr[x1][k-1]
            arr[x1][k] = test
            mini = min(mini, test)
        arr[x1][y1+1] = tmp
        answer.append(mini)
    return answer
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    scores = []
    answer = 1
    top = 0
    for i in range(n):
        paper, interview = map(int, input().split())
        scores.append((paper, interview))
    scores.sort(key= lambda x:x[0])

    for i in range(1, n):
        if scores[i][1] < scores[top][1]:
            top = i
            answer += 1
    print(answer)
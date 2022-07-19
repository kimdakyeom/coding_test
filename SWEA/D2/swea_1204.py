# import sys
# sys.stdin = open("swea_1204_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    test = int(input())
    score = [0] * 101
    max = 0
    grade = 0
    num = list(map(int, input().split()))
    for j in range(len(num)):
        score[num[j]] += 1
    for x in range(1, len(score)):
        if max <= score[x]:
            max = score[x]
            grade = x
    print(f'#{i} {grade}')
# import sys
# sys.stdin = open("swea_1983_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    n, k = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    list = []

    for i in range(1, n+1):
        mid, fin, assign = map(int, input().split())
        score = mid * 0.35 + fin * 0.45 + assign * 0.2
        list.append(score)

    k_score = list[k-1]
    list.sort()
    list.reverse()
    
    for j in range(len(list)):
        if list[j] == k_score:
            deung = j + 1

    for i in range(0, n+1):
        if deung / (n / 10) > i and deung / (n / 10) <= i+1:
            print(f'#{T} {grade[i]}')
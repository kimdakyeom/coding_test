# import sys
# sys.stdin = open("swea_1860_input.txt", 'rt', encoding='UTF8')

T = int(input())

for t in range(1, T+1):
    n, m, k = map(int, input().split())

    person = list(map(int,input().split()))
    person.sort()

    ans = 'Possible'
    for i in range(n):
        bread = (person[i] // m) * k - (i + 1)
        if bread < 0:
            ans = 'Impossible'
            break
    print(f'#{t} {ans}')

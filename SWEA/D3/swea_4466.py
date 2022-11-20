# from pprint import pprint
# import sys
# sys.stdin = open("swea_4466_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    answer = 0
    for i in range(k):
        answer += scores[i]
    print(f'#{tc} {answer}')
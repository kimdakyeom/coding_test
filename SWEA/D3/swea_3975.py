# from pprint import pprint
# import sys
# sys.stdin = open("swea_3975_input.txt", 'rt', encoding='UTF8')

T = int(input())
answer = []
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    if (a/b) > (c/d) :
        answer.append("ALICE")
    elif (a/b) < (c/d) :
        answer.append("BOB")
    else:
        answer.append("DRAW")
for i in range(1, len(answer)+1):
    print(f"#{i} {answer[i-1]}")
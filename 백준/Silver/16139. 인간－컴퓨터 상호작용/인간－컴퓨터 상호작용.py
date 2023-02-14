import sys
# input = sys.stdin.readline

string = input().rstrip()

n = int(input())
for _ in range(n):
    a, s, e = input().split()
    s, e = int(s), int(e)
    answer = 0
    for i in range(s, e+1):
        if str(string[i]) == a:
            answer += 1
    print(answer)
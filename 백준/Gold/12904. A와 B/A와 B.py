import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

answer = 0
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        answer = 1
        break
print(answer)
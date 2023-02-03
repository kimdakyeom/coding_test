import sys
from pprint import pprint
input = sys.stdin.readline

n1, n2 = map(int, input().split())

tmp_ = list(input().rstrip())
n1_ = []
n2_ = []
for i in tmp_:
    n1_.append((i, 1))
n1_.reverse()
tmp__ = list(input().rstrip())
for i in tmp__:
    n2_.append((i, 2))
t = int(input())
origin = n1_ + n2_
count = 0
answer = ''

if t == 0:
    for o in origin:
        answer += o[0]
else:
    for _ in range(t):
        i = 0
        while i < n1+n2-1:
            if origin[i][1] == 1 and origin[i+1][1] == 2:
                origin[i], origin[i+1] = origin[i+1], origin[i]
                i += 1
            i += 1
    for o in origin:
        answer += o[0]

print(answer)

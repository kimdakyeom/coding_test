import sys
from pprint import pprint
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
origin = set(['a', 'n', 't', 'i', 'c'])
alpha = set(chr(i) for i in range(97, 123)) - origin

data = []
for i in range(n):
    data.append(input().rstrip()[4:-4])

def count(data, learn):
    cnt = 0
    for word in data:
        flag = 1
        for w in word:
            if not learn[ord(w)]:
                flag = 0
                break
        if flag == 1:
            cnt += 1
    return cnt

answer = 0
if k >= 5:
    learn = [0] * 123
    for i in origin:
        learn[ord(i)] = 1
    k = k - 5
    pos = combinations(alpha, k)
    for teach in pos:
        for t in teach:
            learn[ord(t)] = 1
        cnt = count(data, learn)
        answer = max(answer, cnt)
        for t in teach:
            learn[ord(t)] = 0
    print(answer)
else:
    print(0)

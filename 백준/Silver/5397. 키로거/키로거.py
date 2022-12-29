import sys
input = sys.stdin.readline

n = int(input())
keys = []
for _ in range(n):
    keys.append(list(input().rstrip()))
stack = []
idx = -1
for k in range(n):
    key = keys[k]
    left = []
    right = []
    for x in key:
        if x == '>':
            if right:
                left.append(right.pop())
        elif x == '<':
            if left:
                right.append(left.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)
    print("".join(left) + "".join(reversed(right)))
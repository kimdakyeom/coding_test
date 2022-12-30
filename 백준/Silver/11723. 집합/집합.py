import sys

input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    m = input().split()
    if len(m) == 1:
        command = m[0]
        if command == 'all':
            s = set([i for i in range(1, 21)])
        elif command == 'empty':
            s = set()
        continue
    else:
        command = m[0]
        x = int(m[1])
        if command == 'add':
            s.add(x)
        elif command == 'remove':
            s.discard(x)
        elif command == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
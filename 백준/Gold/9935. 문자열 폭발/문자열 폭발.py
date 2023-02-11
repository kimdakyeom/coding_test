import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
stack = []
lastC = bomb[-1]

for c in string:
    stack.append(c)
    if c == lastC and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if len(stack):
    print(''.join(stack))
else:
    print("FRULA")
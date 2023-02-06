import sys
from pprint import pprint
input = sys.stdin.readline

string = list(input().rstrip())
stack = []
n = int(input())

for _ in range(n):
    com = input().split()
    if com[0] == 'P':
        string.append(com[1])
    if com[0] == 'L':
        if string:
            stack.append(string.pop())
    if com[0] == 'D':
        if stack:
            string.append(stack.pop())
    if com[0] == 'B':
        if string:
            string.pop()
print(''.join(string) + ''.join(reversed(stack)))
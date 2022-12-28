import sys
input = sys.stdin.readline

n = int(input())
p = input().rstrip().split('*')
start = p[0]
end = p[1]
answer = 'NE'

for i in range(n):
    file = input().rstrip()
    if file[:len(start)] == start and file[-len(end):] == end and len("".join(p)) <= len(file):
        answer = 'DA'
    else:
        answer = 'NE'
    print(answer)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

finding = 'IOI'
n -= 1
answer = 0
for i in range(n):
    finding += 'OI'
for i in range(m - len(finding) + 1):
    if s[i:i+len(finding)] == finding:
        answer += 1
print(answer)
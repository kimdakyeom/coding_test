import sys
input = sys.stdin.readline

n, m = map(int, input().split())

password = {}
for i in range(n):
    site, pw = input().split()
    password[site] = pw

for i in range(m):
    print(password[input().rstrip('\n')])
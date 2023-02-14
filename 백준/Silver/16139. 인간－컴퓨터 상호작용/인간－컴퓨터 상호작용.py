import sys
# input = sys.stdin.readline

string = input().rstrip()

n = int(input())
arr = [[0 for i in range(26)] for i in range(len(string))]
arr[0][ord(string[0])-97] = 1

for i in range(1, len(string)):
    arr[i][ord(string[i])-97] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]
for i in range(n):
    a, s, e = input().split()
    s, e = int(s), int(e)
    if s > 0:
        answer = arr[e][ord(a)-97] - arr[s-1][ord(a)-97]
    else:
        answer = arr[e][ord(a)-97]
    print(answer)
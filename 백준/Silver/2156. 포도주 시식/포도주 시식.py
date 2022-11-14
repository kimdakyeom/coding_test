n = int(input())
d = [0] * 10002
s = [0] * 10002
arr = []

for i in range(1, n+1):
    s[i] = int(input())
d[1] = s[1]
d[2] = s[1] + s[2]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-3] + s[i-1] + s[i], d[i-2] + s[i])
print(d[n])
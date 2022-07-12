a, m, d, n = input().split(" ")
a = int(a)
m = int(m)
d = int(d)
n = int(n)
ans = a
for i in range(0, n-1):
    ans = ans * m + d
print(ans)
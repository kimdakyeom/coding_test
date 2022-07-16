n = []
nam = []
result = []
cnt = 0

for i in range(10) :
    num = int(input())
    n.append(num)

for i in range(10):
    nam.append(n[i] % 42)

for i in nam:
    if i not in result:
        result.append(i)

for i in result:
    cnt += 1
print(cnt)
n, m = map(int, input().split())
arr = [input() for _ in range(n)]

k = int(input())

dict = {}
for a in arr:
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1
dict = list(dict.items())
dict.sort(key=lambda x:-x[1])
answer = 0
for a, n in dict:
    cnt = a.count('0')
    if k >= cnt and (k - cnt) % 2 == 0:
        answer = n
        break
print(answer)
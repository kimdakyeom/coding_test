import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(list(set(x)))
dict_x = {}

for i in range(len(sorted_x)):
    if sorted_x[i] not in dict_x:
        dict_x[sorted_x[i]] = i
    else:
        continue

answer = []
for i in range(len(x)):
    answer.append(dict_x[x[i]])

for i in answer:
    print(i, end=' ')
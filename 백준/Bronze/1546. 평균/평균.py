n = int(input())
list = list(map(int, input().split(" ")))
max = max(list)
new_list = []

for i in list:
    new_list.append(i/max*100)
avg = sum(new_list) / n
print(round(avg, 3))
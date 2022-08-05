n = int(input())
road = list(map(int, input().split()))
tmp = 0
up = []

for i in range(1, n):
    if road[i] > road[i-1]:
        tmp += road[i] - road[i-1]

        if i == n - 1:
            up.append(tmp)
    else:
        up.append(tmp)
        tmp = 0
        
print(max(up))
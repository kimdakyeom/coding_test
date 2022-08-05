n, m = map(int, input().split())

hear = []
see = []
hearsee = {}
ans = []

for i in range(n):
    hear_name = input()
    hear.append(hear_name)

for i in range(m):
    see_name = input()
    see.append(see_name)

for i in hear:
    if i in hearsee:
        hearsee[i] += 1
    else:
        hearsee[i] = 1
    
for i in see:
    if i in hearsee:
        hearsee[i] += 1
    else:
        hearsee[i] = 1

for i in hearsee:
    if hearsee[i] == 2:
        ans.append(i)
ans.sort()

print(len(ans))

for i in ans:
    print(i)
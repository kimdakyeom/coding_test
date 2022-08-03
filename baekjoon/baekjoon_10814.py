n = int(input())
join = []

for i in range(n):
    age, name = input().split()
    join.append([int(age), i, name])
join = sorted(join)

for i in range(n):
    print(join[i][0], join[i][2])
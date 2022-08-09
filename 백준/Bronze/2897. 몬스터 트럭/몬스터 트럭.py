r, c = map(int, input().split())

park = [list(input()) for _ in range(r)]
ans = [0] * 5

for i in range(r-1):
    for j in range(c-1):
        lot = []
        lot.append(park[i][j])
        lot.append(park[i][j+1])
        lot.append(park[i+1][j])
        lot.append(park[i+1][j+1])
        if lot.count('.') == 4:
            ans[0] += 1
        elif lot.count('.') == 3 and lot.count('X') == 1 :
            ans[1] += 1
        elif lot.count('.') == 2 and lot.count('X') == 2 :
            ans[2] += 1
        elif lot.count('.') == 1 and lot.count('X') == 3 :
            ans[3] += 1
        elif lot.count('.') == 0 and lot.count('X') == 4 :
            ans[4] += 1
for i in ans:
    print(i)
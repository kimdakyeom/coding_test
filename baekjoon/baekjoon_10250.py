try_ = int(input())
cnt = 0

for loop in range(try_):
    h, w, n = map(int, input().split(" "))
    for i in range(1, w+1):
        for j in range(1, h+1):
            hosu = str(j) + str(format(i, '02'))
            cnt += 1
            if cnt == n:
                break
        if cnt == n:
                break
    print(hosu)
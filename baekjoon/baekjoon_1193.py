x = int(input())
cnt = 1

for i in range(1, x):
    for j in range(1, i+1):
        for k in range(x, 1):
            for l in range(k+1, 1):
                cnt += 1
                print(f'{j}/{i}')
        #if cnt == x:
        #    print(f'{i}/{j}')
        #    break
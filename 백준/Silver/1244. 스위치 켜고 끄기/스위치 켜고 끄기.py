def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

n = int(input())
switch = [-1] + list(map(int, input().split()))
T = int(input())

for t in range(T):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num, n + 1, num):
            change(i)
    
    if sex == 2:
        change(num)
        
        for i in range(n // 2):
            if num + i > n or num - i < 1:
                break
            if switch[num + i] == switch[num - i]:
                change(num + i)
                change(num - i)
            else:
                break

for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
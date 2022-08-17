n = int(input())

for t in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_cnt = [0] * 5
    b_cnt = [0] * 5

    for i in range(1, len(a)):
        a_cnt[a[i]] += 1
    for i in range(1, len(b)):
        b_cnt[b[i]] += 1
    
    a_cnt = a_cnt[4:0:-1]
    b_cnt = b_cnt[4:0:-1]

    for i in range(4):
        if a_cnt[i] > b_cnt[i]:
            print('A')
            break
        elif a_cnt[i] < b_cnt[i]:
            print('B')
            break
        else:
            continue
    if a_cnt == b_cnt:
        print('D')
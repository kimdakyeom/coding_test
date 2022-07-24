import sys
sys.stdin = open("swea_11736_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    
    tmp = []
    tmp_ = []

    for i in range(len(num)-2):
        for j in range(i, i+3):
            tmp.append(num[j])
    
    for i in range(len(tmp)//3):
        tmp_ = tmp[i:i+3]
        if tmp_[1] != max(tmp_) or tmp_[1] != min(tmp_):
            cnt += 1
    print(f'#{t} {cnt-1}')
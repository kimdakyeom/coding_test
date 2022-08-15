import sys
sys.stdin = open("swea_2948_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    n_list = list(input().split())
    m_list = list(input().split())
    
    dict = {}
    for i in n_list:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    for j in m_list:
        if j not in dict:
            dict[j] = 0
        elif j in dict:
            dict[j] += 1
    
    cnt = 0
    for i in dict:
        if dict.get(i) == 2:
            cnt += 1
    print(f'#{t} {cnt}')
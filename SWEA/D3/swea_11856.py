# import sys
# sys.stdin = open("swea_11856_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    word = input()
    list = []
    alpha = [0] * 27
    cnt = 0

    for i in word:
        n_word = ord(i)
        list.append(n_word-64)
    
    for i in range(len(list)):
        alpha[list[i]] += 1
    
    for i in range(len(alpha)):
        if alpha[i] == 2:
            cnt += 1
    
    if cnt == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')
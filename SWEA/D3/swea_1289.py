# import sys
# sys.stdin = open("swea_1289_input.txt", 'rt', encoding='UTF8')

T = int(input())

for t in range(1, T+1):
    memory = input()

    flag = '0'
    count = 0
    for i in range(len(memory)):
        if memory[i] != flag:
            count += 1
            flag = memory[i]

    print(f'#{t} {count}')
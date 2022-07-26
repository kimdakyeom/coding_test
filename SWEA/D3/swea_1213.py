# import sys
# sys.stdin = open("swea_1213_input.txt", 'rt', encoding='UTF8')

T = 10

for t in range(1, T+1):
    n = int(input())

    find = input()
    sentence = input()

    print(f'#{t} {sentence.count(find)}')
# import sys
# sys.stdin = open("swea_1989_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    word = input()
    k = int(len(word)/2+1)
    l = int(len(word)/2)
    magimak = int(len(word))

    if len(word) % 2 == 1:
        if word[0:k] == word[magimak:k-2:-1]:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
    elif len(word) % 2 == 0:
        if word[0:l] == word[magimak:l-1:-1]:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
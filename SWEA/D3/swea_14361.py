# import sys
# sys.stdin = open("swea_14361_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = list(input())
    int_n = int("".join(n))
    i = 2
    flag = 'impossible'
    new = n

    while True:
        new = list(str(int_n * i))
        i += 1

        if len(new) != len(n):
            break
        if set(new) == set(n):
            flag = 'possible'
            break

    print(f'#{t} {flag}')
# import sys
# sys.stdin = open("swea_1493_input.txt", 'rt', encoding='UTF8')

T = int(input())

for t in range(1, T+1):
    arr = [0 for _ in range(400)]
    for i in range(1, 399):
        arr[i] = arr[i-1] + i

    p, q = map(int, input().split())
    pos = [[], []]

    for i in range(1, len(arr)):
        if not pos[0] and p <= arr[i]:
            gab_p = arr[i] - p
            pos[0] = [1 + gab_p, i - gab_p]
        if not pos[1] and q <= arr[i]:
            gab_q = arr[i] - q
            pos[1] = [1 + gab_q, i - gab_q]
        if pos[0] and pos[1]:
            break

    y = pos[0][0] + pos[1][0]
    x = pos[0][1] + pos[1][1]

    ans = 0

    for i in range(y-1):
        ans += x + i
    print(f'#{t} {arr[x] + ans}')
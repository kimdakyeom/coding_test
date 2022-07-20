# import sys
# sys.stdin = open("swea_1959_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    A, B = map(int, input().split())

    a = list(input().split())
    b = list(input().split())

    max = 0

    for i in range(abs(A - B) + 1):
        ans = 0
        for j in range(min(A, B)):
            if len(a) > len(b):
                ans += int(a[j+i]) * int(b[j])
            elif len(a) < len(b):
                ans += int(b[j+i]) * int(a[j])
            else:
                ans += int(a[j]) * int(b[j])
        if ans > max:
            max = ans
    
    print(f'#{T} {max}')
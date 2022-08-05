import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    a_n = int(input())
    a = set(map(int, input().split()))
    b_n = int(input())
    b = list(map(int, input().split()))

    for i in b:
        if i in a:
            print(1)
        elif i not in a:
            print(0)
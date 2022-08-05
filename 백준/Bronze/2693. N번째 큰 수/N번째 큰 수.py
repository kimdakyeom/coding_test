n = int(input())

for tc in range(n):
    num = list(map(int, input().split()))
    num = sorted(num, reverse=True)
    print(num[2])
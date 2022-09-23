import sys
sys.stdin = open("swea_14413_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input().split(''))
    print(arr)
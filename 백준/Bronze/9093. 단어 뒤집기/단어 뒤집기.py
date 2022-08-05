n = int(input())

for tc in range(n):
    word = list(input().split())
    
    for i in word:
        print(i[::-1], end=' ')
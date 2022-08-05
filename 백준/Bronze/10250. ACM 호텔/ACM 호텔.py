k = int(input())
result = 0

for i in range(k):
    h, w, n = map(int, input().split(" "))
    ch = n % h
    ho = n // h + 1
    if ch == 0:
        ch = h
        ho -= 1
    result = str(ch) + str(format(ho, '02'))
    print(result)
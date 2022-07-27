T = int(input())

for t in range(T):
    wh,word = input().split()
    wh = int(wh)

    word = list(word)

    del word[wh-1]

    result = ''.join(i for i in word)
    print(result)
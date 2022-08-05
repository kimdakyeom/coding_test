n = int(input())
n_card = list(map(int, input().split()))

m = int(input())
m_card = list(map(int, input().split()))

counter = {}

for i in n_card:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for i in m_card:
    if i in counter:
        print(counter[i], end=' ')
    else:
        print(0, end=' ')
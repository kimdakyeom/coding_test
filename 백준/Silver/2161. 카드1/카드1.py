from collections import deque

n = int(input())
card = deque(range(1, n+1))
discard = []

while len(card) > 1:
    discard.append(card.popleft())
    card.append(card.popleft())

for i in discard:
    print(i, end=' ')
print(card[0])
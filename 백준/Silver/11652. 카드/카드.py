n = int(input())

card = []
dict = {}

for i in range(n):
    card_input = int(input())
    card.append(card_input)

for i in card:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

max_ = 0
ans = 0

sort_dict = sorted(dict.items())
for i, cnt in sort_dict:
    if max_ < cnt:
        max_ = cnt
        ans = i
print(ans)
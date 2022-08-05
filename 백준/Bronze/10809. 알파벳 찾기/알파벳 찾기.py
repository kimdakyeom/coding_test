word = input()
list = []

for i in range(26):
    list.append(-1)

for i in word:
    idx = ord(i) - 97
    list[idx] = word.index(i)
print(*list)
word = input()
WORD = word.upper()
list = []

for i in range(27):
    list.append(0)

for i in WORD:
    list[ord(i) - 64] += 1
    tmp = max(list)
    index = chr(list.index(tmp) + 64)
print(index)
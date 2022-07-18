word = input()
WORD = word.upper()
list = []
cnt = 0

for i in range(27):
    list.append(0)

for i in WORD:
    list[ord(i) - 64] += 1
    tmp = max(list)
    index = chr(list.index(tmp) + 64)

for i in range(1, 27):
    if list[i] == tmp:
        cnt += 1
if cnt >= 2:
    print("?")
else:
    print(index)
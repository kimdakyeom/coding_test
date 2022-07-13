list=[]
for i in range(12) :
  list.append([])
  for j in range(12) :
    list[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    list[i+1][j+1]=int(a[j])

x = 2
y = 2

while True:
    if list[x][y] == 0:
        list[x][y] = 9
    elif list[x][y] == 2:
        list[x][y] = 9
        break

    if (list[x][y+1] == 1 and list[x+1][y] == 1) or (x == 9 and y == 9):
        break

    if list[x][y+1] != 1:
        y += 1
    elif list[x+1][y] != 1:
        x += 1

for i in range(1, 11) :
  for j in range(1, 11) :
    print(list[i][j], end=' ')
  print()

  # 너무 어려움.....
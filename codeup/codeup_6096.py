list = []
for i in range(20) :
  list.append([])
  for j in range(20) : 
    list[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    list[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y = input().split()
  x = int(x)
  y = int(y)
  for j in range(1, 20) :
    if list[j][y]==0 :
      list[j][y]=1
    else :
      list[j][y]=0

    if list[x][j]==0 :
      list[x][j]=1
    else :
      list[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(list[i][j], end=' ')
  print()

  # 알고리즘은 대충 알았는데..
  # 구현하는게 너무 힘들다ㅜㅜ
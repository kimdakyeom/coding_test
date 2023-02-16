import sys
input = sys.stdin.readline

def find(parent, x):
	if parent[x] == x:
		return x
	parent[x] = find(parent, parent[x])
	return parent[x]

def union(parent, u, v):
	a = find(parent, u)
	b = find(parent, v)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b

n, m = map(int, input().split())
gender = list(input().split())
edges = []
result = 0
cnt = 0
parent = [0] * (n+1)
for i in range(1, n+1):
	parent[i] = i

for i in range(m):
	u, v, d = map(int, input().split())
	if (gender[u-1] == 'M' and gender[v-1] == 'W') or (gender[u-1] == 'W' and gender[v-1] == 'M'):
		edges.append((d, u, v))
edges.sort()

for edge in edges:
	d, u, v = edge
	if find(parent, u) != find(parent, v):
		union(parent, u, v)
		result += d
		cnt += 1
if cnt == n-1:
	print(result)
else:
	print(-1)
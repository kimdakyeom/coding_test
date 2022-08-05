from collections import deque

n = int(input())

deque_ = deque()

for i in range(1, n+1):
    deque_.append(i)

while len(deque_) > 1:
    deque_.popleft()
    append_data = deque_.popleft()
    deque_.append(append_data)
print(*list(deque_))
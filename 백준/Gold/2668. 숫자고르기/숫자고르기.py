def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, arr[num])

n = int(input())
arr = [0]
answer = set()

for i in range(n):
    arr.append(int(input()))

for i in range(1, n+1):
    if i not in answer:
        dfs(set(), set(), i)
print(len(answer))

for a in (sorted(answer)):
    print(a)
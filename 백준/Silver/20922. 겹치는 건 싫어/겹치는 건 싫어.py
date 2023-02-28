import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
count = [0] * (max(arr) + 1)
answer = 0
while right < n:
    if count[arr[right]] < k:
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
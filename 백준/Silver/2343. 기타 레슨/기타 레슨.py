import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = max(nums)
end = sum(nums)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    sum_nums = 0
    for i in range(n):
        if sum_nums + nums[i] > mid:
            cnt += 1
            sum_nums = 0
        sum_nums += nums[i]
    if sum_nums:
        cnt += 1
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1
print(start)
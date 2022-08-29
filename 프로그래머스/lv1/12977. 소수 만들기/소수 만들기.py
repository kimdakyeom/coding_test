def solution(nums):
    answer = 0

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1 , len(nums)):
                sosu = 0
                for div in range(1, nums[i] + nums[j] + nums[k] + 1):
                    if (nums[i] + nums[j] + nums[k]) % div == 0:
                        sosu += 1
                if sosu == 2:
                    answer += 1
    return answer
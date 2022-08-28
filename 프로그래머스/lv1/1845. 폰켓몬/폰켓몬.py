def solution(nums):
    answer = 0
    length = len(nums) / 2
    tmp = list(set(nums))

    for i in tmp:
        if answer < length:
            answer += 1
    
    return answer
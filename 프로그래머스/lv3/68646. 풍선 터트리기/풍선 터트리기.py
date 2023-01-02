def solution(a):
    answer = 2
    left, right = a[0], a[-1]
    for i in range(len(a)):
        if a[i] < left:
            answer += 1
            left = a[i]
        if a[-1-i] < right:
            answer += 1
            right = a[-1-i]
    return answer if left != right else answer -1
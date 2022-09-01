#You may use import as below.
#import math

def solution(shirt_size):
    answer = [0] * 6
    for i in range(len(shirt_size)):
        if shirt_size[i] == "XS":
            answer[0] += 1
        elif shirt_size[i] == "S":
            answer[1] += 1
        elif shirt_size[i] == "M":
            answer[2] += 1
        elif shirt_size[i] == "L":
            answer[3] += 1
        elif shirt_size[i] == "XL":
            answer[4] += 1
        elif shirt_size[i] == "XXL":
            answer[5] += 1
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
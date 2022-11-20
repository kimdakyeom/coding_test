from math import gcd

def get_gcd(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g

def solution(arrayA, arrayB):
    answer = 0
    a, b = get_gcd(arrayA), get_gcd(arrayB)

    for i in arrayB:
        if i % a == 0:
            break
    else:
        answer = max(a, answer)
    for i in arrayA:
        if i % b == 0:
            break
    else:
        answer = max(b, answer)
    
    return answer
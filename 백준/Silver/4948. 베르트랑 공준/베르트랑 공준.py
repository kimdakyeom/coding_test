import sys
import math
# sys.stdin = open("input.txt", "rt", encoding="UTF8")


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    cnt = 0
    for i in range(n+1, (2*n) + 1):
        if is_prime(i):
            cnt += 1
    print(cnt)
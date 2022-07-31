import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in num:
    if isPrime(i):
        cnt += 1
print(cnt)
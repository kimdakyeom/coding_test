import sys
input = sys.stdin.readline

s, e, q = input().split()
start = s[:2] * 60 + s[-2:]
end = e[:2] * 60 + e[-2:]
streaming = q[:2] * 60 + q[-2:]

stu = set()
answer = 0

while True:
    try:
        t, n = input().split()
        time = t[:2] * 60 + t[-2:]
        if start >= time:
            stu.add(n)
        elif end <= time <= streaming and n in stu:
            stu.remove(n)
            answer += 1
    except:
        break

print(answer)
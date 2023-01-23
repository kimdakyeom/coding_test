import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
bridge = [0]*w
trucks = list(map(int, input().split()))
answer = 0

while bridge:
    answer += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(answer)
# import sys
# sys.stdin = open("swea_1940_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    speed = 0
    move = 0

    for i in range(n):
        arr = list(map(int, input().split()))

        # 가속이면
        if arr[0] == 1:
            # speed에 가속도 더하기
            speed += arr[1]
        # 감속이면
        elif arr[0] == 2:
            # 만약 현재 속도보다 감속할 속도가 더 작을 경우
            if speed > arr[1]:
                # speed에서 가속했던 속도 빼기
                speed -= arr[1]
            # 만약 현재 속도보다 감속할 속도가 더 클 경우
            else:
                # speed는 0으로 초기화
                speed = 0
        # 전체 움직인 거리는 speed 모두 더하기
        move += speed

    print(f"#{t} {move}")
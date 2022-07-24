# import sys
# sys.stdin = open("swea_13038_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    # 나올 수 있는 최댓값으로 초기화
    min_day = n * 7

    for i in range(7):
        # 수업이 열리면
        if arr[i] == 1:
            cnt = 0
            day = 0
            # n일 미만으로 수업을 들었다면 반복
            while(cnt < n):
                # 수업 열리는 날 1씩 더하기
                cnt += arr[(i+day)%7]
                # 삼성대학교에서 지내야하는 날
                day += 1
            # min_day보다 day가 작으면
            if day < min_day:
                # day를 min_day로 바꿈
                min_day = day
    print(f'#{t} {min_day}')
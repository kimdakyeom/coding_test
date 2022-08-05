n = int(input())

# 진행 가능
flag = False

# 지뢰찾기 격자 입력받기
bomb = [list(input()) for _ in range(n)]
# 이미 열어본 격자 입력받기
input_ = [list(input()) for _ in range(n)]
# 빈 answer 리스트 생성
answer = [list(["."] * (n+2)) for _ in range(n+2)]

# bomb의 첫째줄과 마지막 줄에 ["."]으로 채워진 리스트 추가
bomb.insert(0, ["."] * (n+2))
bomb.insert(len(bomb), ["."] * (n+2))

# bomb의 행마다 맨 처음과 맨 마지막에 "." 추가
for i in range(1, n+2):
    bomb[i].insert(0, ".")
    bomb[i].insert(len(bomb[i]), ".")

# input_의 첫째줄과 마지막 줄에 ["."]으로 채워진 리스트 추가
input_.insert(0, ["."] * (n+2))
input_.insert(len(input_), ["."] * (n+2))

# bomb의 행마다 맨 처음과 맨 마지막에 "." 추가
for i in range(1, n+2):
    input_[i].insert(0, ".")
    input_[i].insert(len(input_[i]), ".")

# 1부터 n까지 순회
for i in range(1, n+1):
    for j in range(1, n+1):
        # cnt 0으로 초기화
        cnt = 0
        # input_ 값이 "X"이면
        if input_[i][j] == "x":
            # bomb 값이 "."이면
            # input_[i][j]의 근처 9개 값 확인후
            # "*"이면 cnt에 1씩 더하기
            if bomb[i][j] == ".":
                if bomb[i-1][j-1] == "*":
                    cnt += 1
                if bomb[i-1][j] == "*":
                    cnt += 1
                if bomb[i-1][j+1] == "*":
                    cnt += 1
                if bomb[i][j-1] == "*":
                    cnt += 1
                if bomb[i][j] == "*":
                    cnt += 1
                if bomb[i][j+1] == "*":
                    cnt += 1
                if bomb[i+1][j-1] == "*":
                    cnt += 1
                if bomb[i+1][j] == "*":
                    cnt += 1
                if bomb[i+1][j+1] == "*":
                    cnt += 1
                answer[i][j] = str(cnt)
            # bomb 값이 "*"이면
            elif bomb[i][j] == "*":
                # 진행 불가능
                flag = True
        # input_[i][j]가 "."이면
        if input_[i][j] == ".":
            # "." 출력하기
            answer[i][j] = "."

# 진행이 불가능하면
if flag:
    for i in range(1, n+1):
        for j in range(1, n+1):
            # bomb 값이 "*"이면
            if bomb[i][j] == "*":
                # answer 값을 "*"로 바꿈
                answer[i][j] = "*"

# answer 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(answer[i][j], end= '')
    print()
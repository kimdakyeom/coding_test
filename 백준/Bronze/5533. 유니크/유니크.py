import sys
input = sys.stdin.readline

n = int(input())

# 점수 세개씩 입력 받아서 5번 반복해서 리스트에 저장
score = [list(map(int, input().split())) for _ in range(n)]

# n회 순회
for i in range(n):
    # 점수 변수 초기화
    sum = 0
    # 점수 세개 순회
    for j in range(3):
        # research 리스트에 비교할 세로의 값들 저장
        research = [score[_][j] for _ in range(n)]
        # research 리스트에서 자기 자신 제거
        research.remove(score[i][j])

        # 현재 값이 research 리스트에 없다면
        if score[i][j] not in research:
            # sum에 현재 값 더하기
            sum += score[i][j]
    
    print(sum)
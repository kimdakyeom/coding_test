import sys
sys.stdin = open("swea_2806_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = 0
    chess = [0] * n

    def check(x):
        for i in range(x):
            # 같은 줄, 대각선 확인
            if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
                return False
        return True

    
    def queen(x):
        global answer
        # n번 반복이 끝나면
        if x == n:
            # 답 1씩 증가
            answer += 1 
            return
        else:
            for i in range(n):
                # 배치 가능한 인덱스에 i 넣기
                chess[x] = i
                # 같은 줄, 대각선에 없으면
                if check(x):
                    # 다음 줄로 가서 판단
                    queen(x+1)
    
    # x=0부터 시작
    queen(0)
    print(f'#{tc} {answer}')
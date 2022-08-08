n = int(input())

nth = 666
cnt = 0

while True:
    # 수에 '666'이 포함되어 있다면
    if '666' in str(nth):
        # cnt 올리기
        cnt += 1
    # cnt랑 n번째 수가 같다면
    if cnt == n:
        # nth 출력
        print(nth)
        # while문 빠져나오기
        break
    # '666'이 포함된 수가 나올 때까지 nth를 1씩 증가시키기
    nth += 1
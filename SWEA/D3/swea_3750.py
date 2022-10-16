import sys

sys.stdin = open("swea_3750_input.txt", "rt", encoding="UTF8")

answer = []
for tc in range(1, int(input()) + 1):
    # 문자로 입력받기
    n = input()

    # n 길이가 1이 아닐때 반복
    while len(n) != 1:
        sum_ = 0
        for i in range(len(n)):
            # n의 각 자릿수를 정수형으로 반환해서 sum_에 누적
            sum_ += int(n[i])
        # 누적이 끝나면 문자형으로 변환해서 n에 넣기
        n = str(sum_)
    answer.append(n)

# 해당 테스트 케이스 번호와 값 출력
for idx, value in enumerate(answer):
    print(f"#{idx + 1} {value}")

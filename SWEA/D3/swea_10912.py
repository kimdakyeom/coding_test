# import sys
# sys.stdin = open("swea_10912_input.txt", "rt", encoding="UTF8")

T = int(input())

for tc in range(1, T + 1):
    # word를 리스트로 변환
    word = list(input())
    # 리스트에 있는 알파벳 중복 없이
    alpha = set(word)
    answer = ""
    # 리스트에 있는 알파벳에 접근
    for a in alpha:
        # 알파벳이 홀수개면
        if word.count(a) % 2 != 0:
            # 해당 알파벳 추가
            answer += a
    # 알파벳 정렬
    sorted_answer = "".join(sorted(answer))
    # 홀수개인 알파벳이 없다면
    if len(sorted_answer) == 0:
        # Good 출력
        sorted_answer = "Good"
    print(f"#{tc} {sorted_answer}")

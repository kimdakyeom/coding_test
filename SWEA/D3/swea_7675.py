import sys

sys.stdin = open("swea_7675_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    s = input()
    end = [".", "!", "?"]
    list_ = [0 for _ in range(n)]

    # end에 있는 문자를 모두 ^로 바꾸기
    for i in end:
        s = s.replace(i, "^")
    # ^를 기준으로 찢기
    sen_list = s.split("^")

    # 띄어쓰기 기준으로 찢기
    for i in range(n):
        sen_list[i] = sen_list[i].split()

    for i in range(n):
        for j in range(len(sen_list[i])):
            cnt = 0
            # 단어의 문자 하나씩 점근
            for k in sen_list[i][j]:
                # 대문자면
                if k.isupper():
                    # 횟수 세기
                    cnt += 1
                # 숫자면
                elif k.isdigit():
                    cnt -= 1
            # 대문자는 하나고 나머지는 소문자이면
            if cnt == 1:
                # list의 해당 인덱스에 1씩 추가
                list_[i] += 1

    print(f"#{tc}", end=" ")
    print(*list_)

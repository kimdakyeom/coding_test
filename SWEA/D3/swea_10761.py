import sys

sys.stdin = open("swea_10761_input.txt", "rt", encoding="UTF8")


def dfs(b_index, o_index, time):
    # 파란색이나 주황색 리스트의 길이가 0이 아닐때까지 반복
    while len(b) != 0 or len(o) != 0:
        # 파랑색이면
        if list_[0] == "B":
            # 목표 값 > 현재위치 이면
            if int(list_[1]) - 1 > b_index:
                # 현재 위치에 1 더하기
                b_index += 1
            # 목표 값 < 현재위치 이면
            elif int(list_[1]) - 1 < b_index:
                # 현재 위치에 1 빼기
                b_index -= 1
            # 목표 값 = 현재위치 이면
            else:
                # 리스트에서 해당 문자와 값 빼기
                list_.pop(0)
                list_.pop(0)
                # b리스트에서 값 빼기
                b.pop(0)

            # 오렌지 리스트 길이가 0이 아니면
            if len(o) != 0:
                # 현재위치 > 목표값이면
                if o_index > o[0] - 1:
                    # 현재위치에서 1 빼기
                    o_index -= 1
                # 현재위치 < 목표값이면
                elif o_index < o[0] - 1:
                    # 현재위치에서 1 더하기
                    o_index += 1

        else:
            if int(list_[1]) - 1 > o_index:
                o_index += 1
            elif int(list_[1]) - 1 < o_index:
                o_index -= 1
            else:
                list_.pop(0)
                list_.pop(0)
                o.pop(0)

            if len(b) != 0:
                if b_index > b[0] - 1:
                    b_index -= 1
                elif b_index < b[0] - 1:
                    b_index += 1
        time += 1
    return time


for tc in range(1, int(input()) + 1):
    list_ = list(map(str, input().split()))
    # 첫번째 값 = n
    n = int(list_.pop(0))
    # 파란색, 주황색 리스트 만들기
    b = []
    o = []

    for i in range(n):
        # 파랑색이면
        if list_[2 * i] == "B":
            # b 리스트에 다음값 추가
            b.append(int(list_[2 * i + 1]))
        # 검정색이면
        else:
            # o 리스트에 다음값 추가
            o.append(int(list_[2 * i + 1]))
    print(f"#{tc} {dfs(0, 0, 0)}")

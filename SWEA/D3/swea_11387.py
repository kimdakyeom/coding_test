# import sys
# sys.stdin = open("swea_11387_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input()) + 1):
    d, l, n = map(int, input().split())
    answer = 0
    # 현재 레벨
    i = 0

    while i < n:
        # 몬스터에게 입히는 데미지
        damage = d * (1 + i * (l / 100))
        answer += damage
        # 레벨 1씩 증가시키기
        i += 1
        
    print(f'#{tc} {round(answer)}')
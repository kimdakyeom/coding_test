# import sys
# sys.stdin = open("swea_1244_input.txt")

def change(numbers, count):
    temp = ''
    # numbers 리스트에 있는 temp에 추가하기
    for number in numbers:
        temp += number
    # temp값이 answer에 있으면
    if int(temp) in answer[count]:
        # 넘어가기
        return
    # temp값이 answer에 없으면
    else:
        # answer에 tmp를 정수화해서 넣기
        answer[count].append(int(temp))
    # count가 끝났으면 끝내기
    if count == 0:
        return
    n = len(numbers)

    # 숫자 두개씩 바꿔서 비교
    for i in range(n):
        for j in range(i+1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # count를 한번 었으니 현재 numbers를 넣어서 재귀
            change(numbers, count-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]

for tc in range(1, int(input()) + 1):
    num, cnt = input().split()
    num = list(num)
    answer = [[] for _ in range(int(cnt) + 1)]
    change(num, int(cnt))
    print(f'#{tc} {max(answer[0])}')
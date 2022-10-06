# import sys

# sys.stdin = open("swea_5948_input.txt", "rt", encoding="UTF8")
from itertools import combinations
 
for tc in range(1, int(input()) + 1):
    num = map(int, input().split())
    # 3개 숫자의 모든 조합을 리스트에 저장
    com = list(combinations(num, 3))
    # 3개 숫자를 모두 더한 후 중복을 제거한 후 리스트로 저장
    com = list(set(*[map(sum, com)]))
    # 정렬
    com.sort()
    print(f'#{tc} {com[-5]}')
# import sys

# sys.stdin = open("swea_9480_input.txt", "rt", encoding="UTF8")

alpha = set(list("abcdefghijklmnopqrstuvwxyz"))
for tc in range(1, int(input()) + 1):
    n = int(input())
    words = []
    word_sets = [[]]
    ans = 0

    for i in range(n):
        words.append(input())

    # 단어들로 만들 수 있는 모든 조합 만들기
    for word in words:
        for i in range(len(word_sets)):
            word_sets.append(word_sets[i] + [word])

    # 모든 조합에서
    for word_set in word_sets:
        # 알파벳 탐색
        for a in alpha:
            for word in word_set:
                if a in word:
                    break
            else:
                break
        # 단어 조합에 모든 알파벳이 있으면
        else:
            ans += 1
    print(f"#{tc} {ans}")

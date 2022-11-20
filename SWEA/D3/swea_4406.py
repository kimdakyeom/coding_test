# from pprint import pprint
# import sys
# sys.stdin = open("swea_4406_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input())+1):
    word = input()
    new_word = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    print(f'#{tc} {new_word}')
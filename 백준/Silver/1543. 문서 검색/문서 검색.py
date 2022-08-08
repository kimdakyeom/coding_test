sen = input()
word = input()
# 전체 sen을 word로 자르기
word_split = sen.split(word)

# word로 자른 sen의 길이
print(len(word_split) - 1)
n = int(input())
# ENTER로 첫 문장 시작
enter = str(input())
sum = 0
# 딕셔너리 생성
chat = {}

# 1부터 n-1까지 순회
for i in range(1, n):
    # 입력 받기
    input_ = input()

    # 만약 입력이 ENTER이면
    if input_ == "ENTER":
        # chat 딕셔너리의 아이템에 접근
        for k, v in chat.items():
            # value가 1이면(이미 값이 있으면)
            if v == 1:
                # sum에 1 증가
                sum += 1
        # 새로운 chat 딕셔너리 생성
        chat = {}
        continue
    # 만약 input_이 chat 딕셔너리에 없으면(값을 넣는게 최초면)
    if input_ not in chat:  
        # chat의 input_ 인덱스에 1 생성
        chat[input_] = 1

# chat 딕셔너리 아이템 순회
for k, v in chat.items():
    # 만약 value가 1이면
    if v == 1:
        # sum에 1씩 증가
        sum += 1

print(sum)
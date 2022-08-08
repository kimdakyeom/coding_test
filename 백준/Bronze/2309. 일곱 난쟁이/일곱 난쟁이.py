cm = []

# 입력 받은 값 리스트로 생성
for t in range(9):
    cm.append(int(input()))
# 입력 받은 값 전부 더하기
total = sum(cm)

# 전부 순회
for i in range(8):
    for j in range(i+1, 9):
        # 총계에서 리스트에서 두개의 값을 뺀 값이 100이면
        if total - (cm[i] + cm[j]) == 100:
            # 두 값 저장
            one = cm[i]
            two = cm[j]

# 리스트에서 저장한 두 값 빼기
cm.remove(one)
cm.remove(two)
# 오름차순 정렬
cm.sort()

# 빼고 정렬한 리스트 출력
for i in cm:
    print(i)
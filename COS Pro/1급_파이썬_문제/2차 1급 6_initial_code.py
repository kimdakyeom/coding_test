#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    x, y = 0, 0

    for i in range(len(commands)):
        if commands[i] == 'L':
            x -= 1
        elif commands[i] == 'R':
            x += 1
        elif commands[i] == 'U':
            y += 1
        elif commands[i] == 'D':
            y -= 1
    answer = [x, y]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
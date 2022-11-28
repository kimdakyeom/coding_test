import sys
# sys.stdin = open("input2.txt", "r")

from itertools import permutations
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
operator_input = list(map(int, input().split()))
operator_list = ["+", "-", "*", "/"]
operator = []

for idx, op in enumerate(operator_input):
    for k in range(op):
        operator.append(operator_list[idx])

maximum = -1e8
minimum = 1e8

for op in permutations(operator, n-1):
    answer = num_list[0]
    for i in range(n-1):
        if op[i] == "+":
            answer += num_list[i+1]
        elif op[i] == "-":
            answer -= num_list[i+1]
        elif op[i] == "*":
            answer *= num_list[i+1]
        elif op[i] == "/":
            if answer > 0:
                answer //= num_list[i+1]
            else:
                answer = -answer
                answer //= num_list[i+1]
                answer = -answer
    if answer > maximum:
        maximum = answer
    if answer < minimum:
        minimum = answer
print(maximum)
print(minimum)
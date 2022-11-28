import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
operator_input = list(map(int, input().split()))

maximum = -1e8
minimum = 1e8
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num_list[depth], plus - 1,  minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_list[depth], plus,  minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_list[depth], plus,  minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_list[depth]), plus,  minus, multiply, divide - 1)
        
dfs(1, num_list[0], operator_input[0], operator_input[1], operator_input[2], operator_input[3],)
print(maximum)
print(minimum)
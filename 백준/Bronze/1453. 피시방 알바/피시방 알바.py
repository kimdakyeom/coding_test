n = int(input())
num_list = list(map(int, input().split()))
num_set = set(num_list)

print(len(num_list) - len(num_set))
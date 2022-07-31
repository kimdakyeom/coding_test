import sys

n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))
for i in sorted(num_list):
    sys.stdout.write(str(i) + '\n')
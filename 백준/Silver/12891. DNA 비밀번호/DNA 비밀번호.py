import sys
input = sys.stdin.readline

s, p = map(int, input().split())
string = input()
a, c, g, t = map(int, input().split())
answer = 0
dict_ = {"A":0, "C":0, "G":0, "T":0}
start = string[:p]
for i in start:
    dict_[i] += 1
if dict_['A'] >= a and dict_['C'] >= c and dict_['G'] >= g and dict_['T'] >= t:
    answer += 1

starti = 0
endi = starti + p

for i in range(s-p):
    dict_[string[starti+i]] -= 1
    dict_[string[endi+i]] += 1
    if dict_['A'] >= a and dict_['C'] >= c and dict_['G'] >= g and dict_['T'] >= t:
        answer += 1
print(answer)
import sys
ans=[0]*26
s=sys.stdin.read()

for i in s:
    if i.islower(): 
        ans[ord(i)-97]+=1

for i in range(len(ans)):
    if ans[i]==max(ans): 
        print(chr(97+i),end='')
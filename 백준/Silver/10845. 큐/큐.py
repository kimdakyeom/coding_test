import sys
input = sys.stdin.readline

n = int(input().strip())

queue = []
for i in range(n):
    input_ = input().strip()
    if input_[:4] == 'push':
        queue.append(int(input_[5:]))
    elif input_ == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input_ == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif input_ == 'size':
        print(len(queue))
    elif input_ == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input_ == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    else:
        pass
x = int(input())

line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    top = x
    bottom = line - x + 1
else:
    top = line - x + 1
    bottom = x
print(f'{top}/{bottom}')
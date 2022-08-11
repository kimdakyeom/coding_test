directions = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1, -1)
}

k, s, n = input().split()

kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65

for i in range(int(n)):
    dir = input()
    for j in range(8):
        nkx = kx + directions[dir][0]
        nky = ky + directions[dir][1]
        if nkx == sx and nky == sy:
            nsx = sx + directions[dir][0]
            nsy = sy + directions[dir][1]
        else:
            nsx = sx
            nsy = sy
    if 0 <= nkx < 8 and 0 <= nky < 8 and 0 <= nsx < 8 and 0 <= nsy < 8:
        kx = nkx
        ky = nky
        sx = nsx
        sy = nsy

ans_k = chr(ky+65) + str(8 - kx)
ans_s = chr(sy+65) + str(8 - sx)
print(ans_k)
print(ans_s)
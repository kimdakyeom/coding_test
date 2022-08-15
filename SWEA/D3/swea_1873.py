# import sys
# sys.stdin = open("swea_1873_input.txt", 'rt', encoding='UTF8')

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

command_dict = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' : 4,
'^' : 0, 'v' : 1, '<' : 2, '>': 3, 0 : '^', 1 : 'v', 2 : '<', 3 : '>'}

search_list = ['<', '>', '^', 'v']

for t in range(1, int(input()) + 1):
    h, w = map(int, input().split())
    map_list = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
           if map_list[i][j] in search_list:
                tank_pos = (i, j, command_dict[map_list[i][j]])
                break
        else: 
            continue
        break

    input()
    commands = input()
    for command in commands:
        temp = command_dict[command]
        if temp == 4:
            dy = tank_pos[0] 
            dx = tank_pos[1]
            while True:
                dy += move_list[tank_pos[2]][0]
                dx +=move_list[tank_pos[2]][1]
                if dy < 0 or dy >= h or dx < 0 or dx >= w or map_list[dy][dx] == '#':
                    break
                if map_list[dy][dx] == '*':
                    map_list[dy][dx] = '.'
                    break
        else:
            y = tank_pos[0]
            x = tank_pos[1]
            dy = y + move_list[temp][0]
            dx = x + move_list[temp][1]
            map_list[y][x] = command_dict[temp]
            tank_pos = (y, x, temp)
            if 0 <= dy < h and 0 <= dx < w and map_list[dy][dx] == '.':
                map_list[y][x] = '.'
                map_list[dy][dx] = command_dict[temp]
                tank_pos = (dy, dx, temp)
    print(f'#{t}', end=' ')
    for i in map_list:
        print(''.join(i))
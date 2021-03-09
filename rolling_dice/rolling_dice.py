from collections import deque

# first input line
map_r, map_c, dice_y, dice_x, roll_count = map(int, input().split())
# get map array
map_arr = []
for i in range(map_r):
    info = [int(x) for x in input().split()]
    map_arr.append(info)
# get rolling info
roll_info = [int(x) for x in input().split()]

# initial dice array
dice_r = deque([0, 0, 0, 0])
dice_c = deque([0, 0, 0, 0])


# map to dice, dice to map
def map_dice():
    if map_arr[dice_y][dice_x] == 0:
        map_arr[dice_y][dice_x] = dice_r[0]
    else:
        dice_r[0] = map_arr[dice_y][dice_x]
        dice_c[0] = dice_r[0]
        map_arr[dice_y][dice_x] = 0


# East 1, West 2, North 3, South 4
# changing dice arr by a roll
for i in range(roll_count):
    init_x = dice_x
    init_y = dice_y
    if roll_info[i] == 1:
        if (dice_x + 1) < map_c:
            dice_x += 1
            dice_r.append(dice_r.popleft())
            dice_c[0] = dice_r[0]
            dice_c[2] = dice_r[2]
    elif roll_info[i] == 2:
        if (dice_x - 1) >= 0:
            dice_x -= 1
            dice_r.appendleft(dice_r.pop())
            dice_c[0] = dice_r[0]
            dice_c[2] = dice_r[2]
    elif roll_info[i] == 3:
        if (dice_y - 1) >= 0:
            dice_y -= 1
            dice_c.appendleft(dice_c.pop())
            dice_r[0] = dice_c[0]
            dice_r[2] = dice_c[2]
    else:
        if (dice_y + 1) < map_r:
            dice_y += 1
            dice_c.append(dice_c.popleft())
            dice_r[0] = dice_c[0]
            dice_r[2] = dice_c[2]
    if (init_x != dice_x) or (init_y != dice_y):
        map_dice()
        print(dice_r[2])

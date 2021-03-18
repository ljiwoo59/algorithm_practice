import numpy as np

button = np.zeros(10)


def push_button(b_num, clock):
    if b_num == 0:
        button[0] += 1
        clock[0] += 3
        clock[1] += 3
        clock[2] += 3
    elif b_num == 1:
        button[1] += 1
        clock[3] += 3
        clock[7] += 3
        clock[9] += 3
        clock[11] += 3
    elif b_num == 2:
        button[2] += 1
        clock[4] += 3
        clock[10] += 3
        clock[14] += 3
        clock[15] += 3
    elif b_num == 3:
        button[3] += 1
        clock[0] += 3
        clock[4] += 3
        clock[5] += 3
        clock[6] += 3
        clock[7] += 3
    elif b_num == 4:
        button[4] += 1
        clock[6] += 3
        clock[7] += 3
        clock[8] += 3
        clock[10] += 3
        clock[12] += 3
    elif b_num == 5:
        button[5] += 1
        clock[0] += 3
        clock[2] += 3
        clock[14] += 3
        clock[15] += 3
    elif b_num == 6:
        button[6] += 1
        clock[3] += 3
        clock[14] += 3
        clock[15] += 3
    elif b_num == 7:
        button[7] += 1
        clock[4] += 3
        clock[5] += 3
        clock[7] += 3
        clock[14] += 3
        clock[15] += 3
    elif b_num == 8:
        button[8] += 1
        clock[1] += 3
        clock[2] += 3
        clock[3] += 3
        clock[4] += 3
        clock[5] += 3
    elif b_num == 9:
        button[9] += 1
        clock[3] += 3
        clock[4] += 3
        clock[5] += 3
        clock[9] += 3
        clock[13] += 3
    for i in range(16):
        if clock[i] == 12:
            clock[i] = 0


def unpush_button(b_num, clock):
    if b_num == 0:
        button[0] -= 1
        clock[0] -= 3
        clock[1] -= 3
        clock[2] -= 3
    elif b_num == 1:
        button[1] -= 1
        clock[3] -= 3
        clock[7] -= 3
        clock[9] -= 3
        clock[11] -= 3
    elif b_num == 2:
        button[2] -= 1
        clock[4] -= 3
        clock[10] -= 3
        clock[14] -= 3
        clock[15] -= 3
    elif b_num == 3:
        button[3] -= 1
        clock[0] -= 3
        clock[4] -= 3
        clock[5] -= 3
        clock[6] -= 3
        clock[7] -= 3
    elif b_num == 4:
        button[4] -= 1
        clock[6] -= 3
        clock[7] -= 3
        clock[8] -= 3
        clock[10] -= 3
        clock[12] -= 3
    elif b_num == 5:
        button[5] -= 1
        clock[0] -= 3
        clock[2] -= 3
        clock[14] -= 3
        clock[15] -= 3
    elif b_num == 6:
        button[6] -= 1
        clock[3] -= 3
        clock[14] -= 3
        clock[15] -= 3
    elif b_num == 7:
        button[7] -= 1
        clock[4] -= 3
        clock[5] -= 3
        clock[7] -= 3
        clock[14] -= 3
        clock[15] -= 3
    elif b_num == 8:
        button[8] -= 1
        clock[1] -= 3
        clock[2] -= 3
        clock[3] -= 3
        clock[4] -= 3
        clock[5] -= 3
    elif b_num == 9:
        button[9] -= 1
        clock[3] -= 3
        clock[4] -= 3
        clock[5] -= 3
        clock[9] -= 3
        clock[13] -= 3
    for i in range(16):
        if clock[i] == 12:
            clock[i] = 0
        if clock[i] < 0:
            clock[i] = 12 + clock[i]


def button_dfs(b_pushed, index):
    if index >= 10:
        return b_pushed
    if np.all((clock_arr == 0)):
        temp = 0
        for i in range(10):
            if button[i] != 0 and button[i] != 4:
                temp += button[i]
        if (temp < b_pushed or b_pushed == -1) and temp != 0:
            b_pushed = temp
        return b_pushed

    for i in range(4):
        for j in range(i + 1):
            push_button(index, clock_arr)
        b_pushed = button_dfs(b_pushed, index + 1)
        for j in range(i + 1):
            unpush_button(index, clock_arr)
    return b_pushed


test_num = int(input())
for i in range(test_num):
    clock_arr = np.array([int(x) for x in input().split()])
    for j in range(16):
        if clock_arr[j] == 12:
            clock_arr[j] = 0
    print(int(button_dfs(-1, 0)))
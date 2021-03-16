import numpy as np
test_num = int(input())


def fillmap(total, i, j):
    if np.count_nonzero(map_arr) == 0:
        total += 1
        return total
    if j >= col:
        j = 0
        i += 1
    if i >= row:
        return total
    if map_arr[i, j] == 1:
        flag = 0
        # 0 top left, 1 top right, 2 down left, 3 down right
        if (i - 1) >= 0 and (j - 1) >= 0:
            if map_arr[i - 1, j] == 1 and map_arr[i, j - 1] == 1:
                flag = 1
                map_arr[i, j] = 0
                map_arr[i - 1, j] = 0
                map_arr[i, j - 1] = 0
                total = fillmap(total, i, j + 1)
                flag = 0
                map_arr[i, j] = 1
                map_arr[i - 1, j] = 1
                map_arr[i, j - 1] = 1
        if (i - 1) >= 0 and (j + 1) < col:
            if map_arr[i - 1, j] == 1 and map_arr[i, j + 1] == 1:
                flag = 1
                map_arr[i, j] = 0
                map_arr[i - 1, j] = 0
                map_arr[i, j + 1] = 0
                total = fillmap(total, i, j + 1)
                flag = 0
                map_arr[i, j] = 1
                map_arr[i - 1, j] = 1
                map_arr[i, j + 1] = 1
        if (i + 1) < row and (j - 1) >= 0:
            if map_arr[i, j - 1] == 1 and map_arr[i + 1, j] == 1:
                flag = 1
                map_arr[i, j] = 0
                map_arr[i, j - 1] = 0
                map_arr[i + 1, j] = 0
                total = fillmap(total, i, j + 1)
                flag = 0
                map_arr[i, j] = 1
                map_arr[i, j - 1] = 1
                map_arr[i + 1, j] = 1
        if (i + 1) < row and (j + 1) < col:
            if map_arr[i, j + 1] == 1 and map_arr[i + 1, j] == 1:
                flag = 1
                map_arr[i, j] = 0
                map_arr[i, j + 1] = 0
                map_arr[i + 1, j] = 0
                total = fillmap(total, i, j + 1)
                flag = 0
                map_arr[i, j] = 1
                map_arr[i, j + 1] = 1
                map_arr[i + 1, j] = 1
        if flag == 0:
            total = fillmap(total, i, j + 1)
    else:
        total = fillmap(total, i, j + 1)
    return total


for i in range(test_num):
    row, col = map(int, input().split())
    map_arr = np.empty(shape = [0, col])
    count = 0
    for j in range(row):
        get = [str(x) for x in input()]
        for k in range(col):
            if get[k] == ".":
                get[k] = 1
                count += 1
            else: get[k] = 0
        map_arr = np.append(map_arr, [get], axis = 0)
    if count % 3 != 0:
        print(0)
    else:
        print(fillmap(0, 0, 0))
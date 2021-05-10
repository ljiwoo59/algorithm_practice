t_num = int(input())
for t in range(t_num):
    r, c = map(int, input().split())
    arr = []
    for i in range(r):
        tmp = [x for x in input()]
        arr.append(tmp)


    mem = 0
    row = 0
    col = 0
    dir = 1
    flag = 0
    count = 0
    r_flag = 0
    # 1 right 2 left 3 up 4 down
    while 1:
        if arr[row][col] == '@':
            flag = 1
            break
        elif arr[row][col] == '<':
            dir = 2
        elif arr[row][col] == '>':
            dir = 1
        elif arr[row][col] == '^':
            dir = 3
        elif arr[row][col] == 'v':
            dir = 4
        elif arr[row][col] == '_':
            if mem == 0:
                dir = 1
            else:
                dir = 2
        elif arr[row][col] == '|':
            if mem == 0:
                dir = 4
            else:
                dir = 3
        elif arr[row][col] == '?':
            print("hi")
            if r_flag == 0:
                dir = 1
                r_flag = 1
            elif r_flag == 1:
                dir = 2
                r_flag = 2
            elif r_flag == 2:
                dir = 3
                r_flag = 3
            elif r_flag == 3:
                dir = 4
                r_flag = 0
        elif arr[row][col] == '.':
            continue
        elif arr[row][col].isdigit():
            mem = int(arr[row][col])
        elif arr[row][col] == '+':
            if mem == 15:
                mem = 0
            else:
                mem += 1
        elif arr[row][col] == '-':
            if mem == 0:
                mem = 15
            else:
                mem -= 1
        if dir == 1:
            if col == c - 1:
                col = 0
            else:
                col += 1
        elif dir == 2:
            if col == 0:
                col = c - 1
            else:
                col -= 1
        elif dir == 3:
            if row == 0:
                row = r - 1
            else:
                row -= 1
        elif dir == 4:
            if row == r - 1:
                row = 0
            else:
                row += 1
        if count >= 500:
            break
        count += 1

    if flag == 1:
        print("#", t + 1, " ", "YES", sep="")
    else:
        print("#", t + 1, " ", "NO", sep="")

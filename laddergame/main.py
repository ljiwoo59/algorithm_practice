def next_col(row, col, array) :
    if col < 99 and array[row][col + 1] == '1' :
        while col < 99 and array[row][col + 1] == '1' :
            col = col + 1
        return col
    elif col > 0 and array[row][col - 1] == '1' :
        while col > 0 and array[row][col - 1] == '1' :
            col = col - 1
        return col
    else :
        return col

array = []
t_num = input()

for i in range(100) :
    str = input().split()
    array.append(str)

for init_col in range(100) :
    if array[0][init_col] == '1' :
        col = init_col
        for row in range(1, 100) :
            col = next_col(row, col, array)
        if array[row][col] == '2' :
            print("#", t_num, " ", init_col)
            break
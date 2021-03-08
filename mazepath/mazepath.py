t_num = input()

arr = []
for i in range(16) :
    str = [int(x) for x in input()]
    arr.append(str)

for row in range(16) :
    col = 0
    for col in range(16) :
        if arr[row][col] == 2 :
            start_r = row
            start_c = col
        elif arr[row][col] == 3 :
            end_r = row
            end_c = col
#EWSN
def non_visited(arr1, arr2, row ,col) :
    if arr1[row][col + 1] != 1:
        arr2.append([row, col + 1])
    if arr1[row][col - 1] != 1:
        arr2.append([row, col - 1])
    if arr1[row - 1][col] != 1:
        arr2.append([row - 1, col])
    if arr1[row + 1][col] != 1:
        arr2.append([row + 1, col])
    return arr2

non_visit = []
non_visit = non_visited(arr, non_visit, start_r, start_c)
flag = 0
while len(non_visit) != 0 :
    arr[start_r][start_c] = 1
    visit = non_visit.pop(len(non_visit) - 1)
    if visit[0] == end_r and visit[1] == end_c :
        flag = 1
        break
    arr[visit[0]][visit[1]] = 1
    non_visit = non_visited(arr, non_visit, visit[0], visit[1])

if flag == 1 :
    print("#", t_num, " ", 1)
else :
    print("#", t_num, " ", 0)
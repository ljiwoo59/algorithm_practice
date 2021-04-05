for test_n in range(10):
    col_n = int(input())
    arr = []
    for i in range(100):
        arr.append([int(x) for x in input().split()])

    def magnetic(arr):
        temp = arr
        for i in range(100):
            for j in range(100):
                if temp[0][j] == 2:
                    temp[0][j] = 0
                elif temp[99][j] == 1:
                    temp[99][j] = 0
                if temp[i][j] == 1 and temp[i + 1][j] == 0:
                    temp[i][j] = 0
                    temp[i + 1][j] = 1
                elif temp[i][j] == 2 and temp[i - 1][j] == 0:
                    temp[i][j] = 0
                    temp[i - 1][j] = 2

        if arr == temp:
            return arr
        magnetic(temp)

    arr = magnetic(arr)
    # count conflict
    count = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and arr[i + 1][j] == 2:
                count += 1

    print("#", test_n + 1, count)
for i in range(10):
    t_num = int(input())
    arr = []
    for i in range(100):
        arr.append([int(x) for x in input().split()])

    sum_v = [0] * 202
    # row sum
    for i in range(100):
        sum_v[i] = sum(arr[i])
    # col sum
    k = 100
    for i in range(100):
        sum_c = 0
        for j in range(100):
            sum_c += arr[j][i]
        sum_v[k] = sum_c
        k += 1
    # left diagonal sum
    for i in range(100):
        sum_v[k] += arr[i][i]
    k += 1
    # right diagonal sum
    sum_rd = 0
    for i in range(100):
        sum_rd += arr[i][99 - i]
    sum_v[k] = sum_rd

    print("#", t_num, max(sum_v))
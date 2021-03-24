test_num = int(input())
for i in range(test_num):
    f_num = int(input())
    f_arr = [int(x) for x in input().split()]
    max_width = [0] * f_num
    max_n = 0
    for i in range(f_num):
        for j in range(f_num):
            if f_arr[j] >= f_arr[i]:
                max_width[j] = f_arr[i]
                if f_arr[j - 1] >= f_arr[i] and j != 0:
                    max_width[j] += max_width[j - 1]
        if max(max_width) > max_n:
            max_n = max(max_width)
    print(max_n)
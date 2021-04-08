test_n = int(input())

for t in range(test_n):
    num, h = map(int, input().split())
    arr_h = [int(x) for x in input().split()]

    min_v = 987654321
    for i in range(2 ** num):
        total = 0
        for j in range(num):
            if i & (1 << j):
                total += arr_h[j]
        if total >= h:
            if min_v > total:
                min_v = total

    print("#", t + 1, " ", min_v - h, sep = "")
for test_n in range(10):
    test_l, arr = map(int, input().split())
    arr = list(map(int, str(arr)))

    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)
            arr.pop(i)
            i = -1
        i += 1

    arr = int("".join([str(x) for x in arr]))
    print("#", test_n + 1, " ", arr, sep = "")
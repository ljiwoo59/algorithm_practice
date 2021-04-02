for i in range(10):
    arr_l = int(input())
    arr = [int(x) for x in input().split()]
    view = 0
    for i in range(2, arr_l - 2):
        if arr[i - 1] < arr[i] and arr[i - 2] < arr[i] and arr[i + 1] < arr[i] and arr[i + 2] < arr[i]:
            view += min(arr[i] - arr[i - 1], arr[i] - arr[i - 2], arr[i] - arr[i + 1], arr[i] - arr[i + 2])
    print(view)
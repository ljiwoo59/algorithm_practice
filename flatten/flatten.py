for i in range(10):
    dump_n = int(input())
    arr = [int(x) for x in input().split()]
    for i in range(dump_n):
        if (max(arr) - min(arr)) <= 1:
            break;
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    print(max(arr) - min(arr))
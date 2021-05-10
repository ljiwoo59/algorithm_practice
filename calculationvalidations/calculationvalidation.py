for t in range(10):
    n = int(input())
    arr = [-1] * (n + 1)

    for i in range(1, n + 1):
        arr[i] = input().split()
        arr[i].pop(0)
        while len(arr[i]) != 1:
            arr[i].pop()

    if n % 2 == 0:
        answer = 0
    else:
        flag = 0
        for i in range(n, 2, -2):
            if arr[i][0].isdigit() and arr[i - 1][0].isdigit() and not arr[i // 2][0].isdigit():
                arr[i // 2] = '1'
            else:
                flag = 1
                break
        if flag == 1:
            answer = 0
        else:
            answer = 1

    print('#', t + 1, ' ', answer, sep="")
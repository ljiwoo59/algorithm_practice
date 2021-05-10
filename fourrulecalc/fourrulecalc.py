for t in range(10):
    n = int(input())
    arr = [-1] * (n + 1)

    for i in range(1, n + 1):
        arr[i] = input().split()
        arr[i].pop(0)
        if len(arr[i]) == 1:
            arr[i] = [int(arr[i][0])]


    def calculation(x):
        if len(arr[x]) == 1:
            return arr[x][0]
        if arr[x][0] == '+':
            return calculation(int(arr[x][1])) + calculation(int(arr[x][2]))
        elif arr[x][0] == '-':
            return calculation(int(arr[x][1])) - calculation(int(arr[x][2]))
        elif arr[x][0] == '/':
            return calculation(int(arr[x][1])) / calculation(int(arr[x][2]))
        elif arr[x][0] == '*':
            return calculation(int(arr[x][1])) * calculation(int(arr[x][2]))


    print("#", t + 1, " ", int(calculation(1)), sep="")
for t in range(10):
    n = int(input())
    arr = [-1] * (n + 1)
    answer = []

    for i in range(1, n + 1):
        arr[i] = input().split()
        arr[i].pop(0)


    def inorder(x):
        if len(arr[x]) == 1:
            answer.append(arr[x][0])
            return
        inorder(x * 2)
        answer.append(arr[x][0])
        if (x * 2 + 1) <= n:
            inorder(x * 2 + 1)


    inorder(1)
    answer = "".join(answer)
    print("#", t + 1, " ", answer, sep="")
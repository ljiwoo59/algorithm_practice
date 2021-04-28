for t_num in range(10):
    d_l, start = map(int, input().split())
    tmp = [int(x) for x in input().split()]

    tmp_arr = []
    tree_arr = []
    for i in range(len(tmp)):
        tmp_arr.append(tmp[i])
        if len(tmp_arr) == 2:
            tree_arr.append(tmp_arr)
            tmp_arr = []

    visited = [-1] * 101
    queue = [start]


    while 1:
        tmp = []
        for j in range(len(queue)):
            for i in range(len(tree_arr)):
                if tree_arr[i][0] == queue[j] and visited[tree_arr[i][1]] == -1:
                    tmp.append(tree_arr[i][1])
                    visited[tree_arr[i][1]] = 1

        if not tmp:
            answer = max(queue)
            break
        else:
            for i in range(len(queue) - 1, -1, -1):
                queue.pop()
            queue.extend(tmp)

    print("#", t_num + 1, " ", answer, sep="")
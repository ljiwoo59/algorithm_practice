for t_num in range(10):
    t_v, t_e = map(int, input().split())
    tmp = [int(x) for x in input().split()]

    e_arr = []
    tmp_arr = []
    for i in range(len(tmp)):
        tmp_arr.append(tmp[i])
        if len(tmp_arr) == 2:
            e_arr.append(tmp_arr)
            tmp_arr = []

    parent_arr = [-1] * (t_v + 1)
    answer = []


    def find_parent(x):
        if parent_arr[x] == -1:
            return -1
        elif parent_arr[x] == x:
            return x
        else:
            return find_parent(parent_arr[x])


    time = t_v
    while time:
        parent_arr = [-1] * (t_v + 1)
        for i in range(len(e_arr)):
            if parent_arr[e_arr[i][0]] == -1:
                parent_arr[e_arr[i][0]] = e_arr[i][0]
            if parent_arr[e_arr[i][1]] == -1:
                parent_arr[e_arr[i][1]] = e_arr[i][0]
            if parent_arr[e_arr[i][0]] != -1:
                parent_arr[e_arr[i][0]] = find_parent(e_arr[i][0])
            if parent_arr[e_arr[i][1]] != -1:
                parent_arr[e_arr[i][1]] = find_parent(e_arr[i][0])
        for i in range(len(parent_arr)):
            parent_arr[i] = find_parent(parent_arr[i])

        for i in range(len(parent_arr)):
            if parent_arr[i] != -1:
                answer.append(parent_arr[i])
                for j in range(len(e_arr) - 1, -1, -1):
                    if e_arr[j][0] == parent_arr[i]:
                        e_arr.pop(j)
                break
        time -= 1

    for i in range(1, t_v + 1):
        if i not in answer:
            answer.append(i)

    print("#", t_num + 1, " ", sep="", end="")
    for i in range(len(answer)):
        print(answer[i], end = " ")
    print()

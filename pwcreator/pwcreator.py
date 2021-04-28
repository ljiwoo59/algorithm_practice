for t in range(10):
    t_num = int(input())
    pw = [int(x) for x in input().split()]

    i = 1
    while 1:
        if i == 6:
            i = 1
        tmp = pw.pop(0)
        tmp -= i
        if tmp <= 0:
            tmp = 0
            pw.append(tmp)
            break
        pw.append(tmp)
        i += 1

    print("#", t_num, " ", " ".join(map(str, pw)), sep="")
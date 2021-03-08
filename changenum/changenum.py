t_count = int(input())

for t_num in range(t_count) :
    num, count = map(int, input().split())
    num = [int(x) for x in str(num)]
    max = -1
    for i in range(len(num)) :
        if max <= num[i] :
            max = num[i]
            max_index = i

    i = 0
    while count != 0 :
        if max_index == i:
            if i < len(num) - 1 :
                count += 1
                i += 1
            elif i == len(num) - 1 and count <= len(num) - 1 :
                temp = num[i]
                num[i] = num[i - 1]
                num[i - 1] = temp
        else :
            temp = num[i]
            num[i] = num[max_index]
            num[max_index] = temp
            if max == num[i - 1] :
                count += 1
            i += 1
        max = -1
        for j in range(i, len(num)) :
            if max <= num[j] :
                max = num[j]
                max_index = j
        count -= 1

    strs = [str(integer) for integer in num]
    a_str = "".join(strs)
    a_int = int(a_str)
    print("#", t_num + 1, " ", a_int)



"""    
    j = 0
    for i in range(count) :
        if max_index != 0 :
            temp = num[j]
            num[j] = num[max_index]
            num[max_index] = temp
            j += 1
        max = -1
        k = j
        while k < len(num) :
            if max <= num[k] and k == j :
                k += 1
                j += 1
            if max <= num[k] :
                max = num[k]
                max_index = k
            k += 1
    print(num)
"""






from itertools import product

t_num = int(input())
calc = [int(x) for x in input().split()]
num_arr = [int(x) for x in input()]
num_d = int("".join(map(str, num_arr)))

flag = 0
count = 1
for i in range(len(num_arr)):
    if calc[num_arr[i]] == 0:
        flag = 1
        break
if flag == 0:
    count += len(num_arr)

else:
    ava_num = []
    for i in range(len(calc)):
        if calc[i] == 1:
            ava_num.append(i)
    perm1 = [p for p in product(ava_num, repeat=1)]
    perm2 = [p for p in product(ava_num, repeat=2)]
    perm3 = [p for p in product(ava_num, repeat=3)]
    perm4 = [p for p in product(ava_num, repeat=4)]
    for i in range(len(perm1) - 1, -1, -1):
        if perm1[i][0] == 0 or perm1[i][0] == 1:
            perm1.pop(i)
        else:
            perm1[i] = int("".join(map(str, perm1[i])))
            if perm1[i] > (num_d // 2) or num_d % perm1[i] != 0:
                perm1.pop(i)
    for i in range(len(perm2) - 1, -1, -1):
        if perm2[i][0] == 0:
            perm2.pop(i)
        else:
            perm2[i] = int("".join(map(str, perm2[i])))
            if perm2[i] > (num_d // 2) or num_d % perm2[i] != 0:
                perm2.pop(i)
    for i in range(len(perm3) - 1, -1, -1):
        if perm3[i][0] == 0:
            perm3.pop(i)
        else:
            perm3[i] = int("".join(map(str, perm3[i])))
            if perm3[i] > (num_d // 2) or num_d % perm3[i] != 0:
                perm3.pop(i)
    for i in range(len(perm4) - 1, -1, -1):
        if perm4[i][0] == 0:
            perm4.pop(i)
        else:
            perm4[i] = int("".join(map(str, perm4[i])))
            if num_d % perm4[i] != 0 or perm4[i] > (num_d//2):
                perm4.pop(i)
    divisor = []
    divisor.extend(perm1)
    divisor.extend(perm2)
    divisor.extend(perm3)
    divisor.extend(perm4)
    divisor.sort(reverse=True)
    answer = []


    def find_answer(num):
        if num == num_d:
            return num
        elif num > num_d:
            div = answer.pop()
            return num // div
        for i in range(len(divisor)):
            num *= divisor[i]
            answer.append(divisor[i])
            num = find_answer(num)
        return num


    find_answer(1)
    print(answer)
"""
    b_flag = 0
    if len(num_arr) >= 4:
        for i in range(len(perm4) - 1, -1, -1):
            if num_d >= perm4[i] and num_d % perm4[i] == 0:
                num_count.append(perm4[i])
                num_d /= perm4[i]
                count += 5
                if num_d == 1:
                    b_flag = 1
                    break
        if b_flag != 1:
            for i in range(len(perm3) - 1, -1, -1):
                if num_d >= perm3[i] and num_d % perm3[i] == 0:
                    num_count.append(perm3[i])
                    num_d /= perm3[i]
                    count += 4
                    if num_d == 1:
                        b_flag = 1
                        break
        if b_flag != 1:
            for i in range(len(perm2) - 1, -1, -1):
                if num_d >= perm2[i] and num_d % perm2[i] == 0:
                    num_count.append(perm2[i])
                    num_d /= perm2[i]
                    count += 3
                    if num_d == 1:
                        b_flag = 1
                        break
        if b_flag != 1:
            for i in range(len(perm1) - 1, -1, -1):
                if num_d >= perm1[i] and num_d % perm1[i] == 0:
                    num_count.append(perm1[i])
                    num_d /= perm1[i]
                    count += 2
                    if num_d == 1:
                        b_flag = 1
                        break

    elif len(num_arr) >= 3:
        for i in range(len(perm3) - 1, -1, -1):
            if num_d >= perm3[i] and num_d % perm3[i] == 0:
                num_count.append(perm3[i])
                num_d /= perm3[i]
                count += 4
                if num_d == 1:
                    b_flag = 1
                    break
        if b_flag != 1:
            for i in range(len(perm2) - 1, -1, -1):
                if num_d >= perm2[i] and num_d % perm2[i] == 0:
                    num_count.append(perm2[i])
                    num_d /= perm2[i]
                    count += 3
                    if num_d == 1:
                        b_flag = 1
                        break
        if b_flag != 1:
            for i in range(len(perm1) - 1, -1, -1):
                if num_d >= perm1[i] and num_d % perm1[i] == 0:
                    num_count.append(perm1[i])
                    num_d /= perm1[i]
                    count += 2
                    if num_d == 1:
                        b_flag = 1
                        break

    elif len(num_arr) >= 2:
        for i in range(len(perm2) - 1, -1, -1):
            if num_d >= perm2[i] and num_d % perm2[i] == 0:
                num_count.append(perm2[i])
                num_d /= perm2[i]
                count += 3
                if num_d == 1:
                    b_flag = 1
                    break
        if b_flag != 1:
            for i in range(len(perm1) - 1, -1, -1):
                if num_d >= perm1[i] and num_d % perm1[i] == 0:
                    num_count.append(perm1[i])
                    num_d /= perm1[i]
                    count += 2
                    if num_d == 1:
                        b_flag = 1
                        break

    elif len(num_arr) >= 1:
        for i in range(len(perm1) - 1, -1, -1):
            if num_d >= perm1[i] and num_d % perm1[i] == 0:
                num_count.append(perm1[i])
                num_d /= perm1[i]
                count += 2
                if num_d == 1:
                    b_flag = 1
                    break
    if b_flag == 0:
        count = -1

    print(num_count)
    print(count)
"""
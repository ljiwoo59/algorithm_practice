for test_n in range(10):
    test_l = int(input())
    arr = list(input())
    temp = []

    flag = 0
    for i in range(test_l):
        if arr[i] == ')':
            if temp.pop() != '(':
                flag = 1
                break
        elif arr[i] == ']':
            if temp.pop() != '[':
                flag = 1
                break
        elif arr[i] == '}':
            if temp.pop() != '{':
                flag = 1
                break
        elif arr[i] == '>':
            if temp.pop() != '<':
                flag = 1
                break
        else:
            temp.append(arr[i])

    if flag == 0:
        print("#", test_n + 1, " ", 1, sep = "")
    else:
        print("#", test_n + 1, " ", 0, sep = "")
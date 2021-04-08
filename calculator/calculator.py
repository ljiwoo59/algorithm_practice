for test_n in range(10):
    test_l = int(input())
    ori_arr = list(input())

    # postfix
    stack = []
    post_arr = []
    for i in range(test_l):
        if ori_arr[i].isdigit():
            post_arr.append(ori_arr[i])
        elif not stack:
            stack.append(ori_arr[i])
        elif ori_arr[i] == ')':
            while stack[-1] != '(':
                post_arr.append(stack.pop())
            stack.pop()
        elif ori_arr[i] == '*':
            while stack[-1] == '*':
                post_arr.append(stack.pop())
            stack.append(ori_arr[i])
        elif ori_arr[i] == '+':
            while stack[-1] == '+' or stack[-1] == '*':
                post_arr.append(stack.pop())
            stack.append(ori_arr[i])
        elif ori_arr[i] == '(':
            stack.append(ori_arr[i])

    # calculation
    stack = []
    for i in range(len(post_arr)):
        if post_arr[i].isdigit():
            stack.append(int(post_arr[i]))
        else:
            if post_arr[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif post_arr[i] == '*':
                stack.append(stack.pop() * stack.pop())

    print("#", test_n + 1, " ", stack.pop(), sep = "")
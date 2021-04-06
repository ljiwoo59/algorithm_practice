for t_n in range(10):
    test_n = int(input())
    arr = []
    for i in range(100):
        arr.append(list(input()))

    for length in reversed(range(101)):
        answer = 0
        # row palindrome
        for row in range(100):
            for col in range(100 - length + 1):
                temp = []
                for i in range(length):
                    temp.append(arr[row][col + i])
                if temp == temp[::-1]:
                    answer = length
                    break
            if answer != 0:
                break
        if answer != 0:
            break
        # col palindrome
        for col in range(100):
            for row in range(100 - length + 1):
                temp = []
                for i in range(length):
                    temp.append(arr[row + i][col])
                if temp == temp[::-1]:
                    answer = length
                    break
            if answer != 0:
                break
        if answer != 0:
            break

    print("#", test_n, answer)

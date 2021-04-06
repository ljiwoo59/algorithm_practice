for test_n in range(10):
    length = int(input())
    arr = []
    for i in range(8):
        arr.append(list(input()))

    count = 0
    # row palindrome
    for row in range(8):
        for col in range(8 - length + 1):
            temp = []
            for l in range(length):
                temp.append(arr[row][col + l])
            if temp == temp[::-1]:
                count += 1
    # col palindrome
    for col in range(8):
        for row in range(8 - length + 1):
            temp = []
            for l in range(length):
                temp.append(arr[row + l][col])
            if temp == temp[::-1]:
                count += 1

    print("#", test_n, count)
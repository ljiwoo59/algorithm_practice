test_n = int(input())


def check(index):
    for i in range(len(arr)):
        for j in range(2):
            for k in range(2):
                if arr[i][j] == pair_arr[index][k]:
                    return 0
    return 1


def pair_comb(count):
    if len(arr) == num / 2:
        count += 1
        return count
    if not arr:
        start = 0
    else:
        start = pair_arr.index(arr[-1]) + 1
    for i in range(start, pair):
        if check(i):
            arr.append(pair_arr[i])
            count = pair_comb(count)
            arr.pop()
    return count


for i in range(test_n):
    num, pair = map(int, input().split())
    get = []
    get = list(map(int, input().split()))
    pair_arr = [get[i:i + 2] for i in range(0, pair * 2, 2)]
    arr = []
    count = pair_comb(0)
    print(count)
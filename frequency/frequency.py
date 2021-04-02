test_t = int(input())
for i in range(test_t):
    test_n = int(input())
    arr = [int(x) for x in input().split()]
    freq = [0] * 101
    for i in range(101):
        freq[i] = arr.count(i)
    print("#", test_n, " ", max([i for i, x in enumerate(freq) if x == max(freq)]))
size = int(input())
arr = []
for i in range(size):
    line = [int(x) for x in input().split()]
    arr.append(line)

for i in reversed(range(size - 1)):
    for j in range(i + 1):
        arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1])

print(arr[0][0])
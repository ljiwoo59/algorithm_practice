def quadtree(arr, index):
    count = 0
    change = 0
    while index < len(map_arr):
        if map_arr[index] == "x" and len(arr) == 0:
            arr.append(map_arr[index])
            index = quadtree(arr, index + 1)
        elif count == 3:
            if change < index - 1:
                arr.append(map_arr[index - change - 2])
                if map_arr[index - change - 2] == "x":
                    index = quadtree(arr, index - change - 1) + 2
            else:
                arr.append(map_arr[index - 2])
                if map_arr[index - 2] == "x":
                    index = quadtree(arr, index - 1) + 2
            for j in range(4):
                map_arr.pop(index - j)
            return index - 4
        else:
            if count == 0:
                j = index
                while j < index + 2:
                    if map_arr[j] == "x":
                        index += 4
                        change += 4
                    j += 1
                arr.append(map_arr[index + 2])
                if map_arr[index + 2] == "x":
                    index = quadtree(arr, index + 3) - 2
            elif count == 1:
                arr.append(map_arr[index + 2])
                if map_arr[index + 2] == "x":
                    index = quadtree(arr, index + 3) - 2
            elif count == 2:
                arr.append(map_arr[index - change - 2])
                if map_arr[index - change - 2] == "x":
                    index = quadtree(arr, index - change - 1) + 2
                    change = 0
            count += 1
        index += 1


test_num = int(input())
for i in range(test_num):
    map_arr = [char for char in input()]
    if len(map_arr) == 1:
        print(map_arr[0])
    else:
        map_chgd = []
        count = 0
        quadtree(map_chgd, 0)
        for i in map_chgd:
            print(i, end="")
def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = mergesort(arr[:mid])
    high_arr = mergesort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def mergesort2(arr):
    def sort(low, high):
        if (high - low) < 2:
            return
        mid = (high + low) // 2
        sort(low, mid)
        sort(mid, high)
        merge(arr, low, mid, high)
        return arr

    def merge(arr, low, mid, high):
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


num_arr = [int(x) for x in input().split()]
print(mergesort(num_arr))
print(mergesort2(num_arr))
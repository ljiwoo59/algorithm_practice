arr1 = [-1] * 100
arr2 = [-1] * 100

t_num, line_num = map(int, input().split())
num_list = [int(x) for x in input().split()]

i = 0
#f_node = 0
flag = 0
while i < len(num_list) :
    if arr1[(num_list[i])] == -1 :
        arr1[(num_list[i])] = num_list[i + 1]
    else :
        arr2[(num_list[i])] = num_list[i + 1]
    """
    if num_list[i + 1] == 99 :
        f_node = num_list[i]
        dst = 99
    """
    i += 2
"""
if f_node == 0:
    flag = -1
"""

non_visit = [arr1[0], arr2[0]]
while len(non_visit) != 0 :
    visit = non_visit.pop(len(non_visit) - 1)
    if visit == 99 :
        flag = 1
        break
    elif visit != -1 :
        non_visit.append(arr1[visit])
        non_visit.append(arr2[visit])

if flag == 1 :
    print("#", t_num, " ", "Yes")
else :
    print("#", t_num, " ", "No")

#Code below is bad code
"""
def node_check(arr1, arr2, f_node) :
    global dst
    for i in range(100) :
        if arr1[i] == f_node :
            dst = arr1[i]
            return i
        elif arr2[i] == f_node :
            dst = arr2[i]
            return i
    return -1

while f_node != 0 :
    if arr1[f_node] == dst :
        f_node = node_check(arr1, arr2, f_node)
    elif arr2[f_node] == dst :
        f_node = node_check(arr1, arr2, f_node)
    if f_node == -1:
        flag = -1
        break

if flag == -1 :
    print("#", t_num, " ", "No")
else :
    print("#", t_num, " ", "Yes")
"""
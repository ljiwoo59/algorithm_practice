# get total count, available weight
total, total_w = map(int, input().split())
# get weight, value
w = []
v = []
for i in range(total):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

# DP
d = [0] * (total_w + 1)
for i in range(total):
    if w[i] <= total_w:
        for j in reversed(range(w[i], total_w + 1)):
            if (w[i]) <= j:
                d[j] = max(d[j], d[j - w[i]] + v[i])

print(d[total_w])
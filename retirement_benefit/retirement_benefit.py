# get total days
days = int(input())
# get available counseling period and benefit
# set benefit as 0 if counseling period overs days
p = []
b = []
for i in range(days):
    period, benefit = map(int, input().split())
    p.append(period)
    b.append(benefit)

# DP
d = [0] * (days + 1)
for i in range(days):
    if d[i] == 0:
        d[i] = d[i - 1]
    d[i] = max(d[i], d[i - 1])
    if (i + p[i]) <= days:
        d[i + p[i]] = max(d[i] + b[i], d[i + p[i]])

print(max(d))








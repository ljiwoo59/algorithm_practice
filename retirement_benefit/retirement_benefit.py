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
    if (i + p[i]) <= days:
        for j in range(i + p[i], days + 1):
            d[j] = max(d[i] + b[i], d[j])

print(d[days])
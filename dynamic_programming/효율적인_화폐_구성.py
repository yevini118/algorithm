n, m = map(int, input().split())

moneys = []
for i in range(n):
    moneys.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for money in moneys:
    for i in range(money, m+1):
        if d[i-money] != 10001:
            d[i] = min(d[i], d[i-money] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



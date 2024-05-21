N = int(input())
candies = dict()
total = 0
zero = 1
for _ in range(N):
    price = int(input())
    if price:
        candies[price] = candies.get(price, 0) + 1
        total += price
    else:
        zero += 1
dp = [0] * (total + 1)
dp[0] = 1
M = 0
for price, cnt in candies.items():
    for i in range(M, -1, -1):
        for j in range(1, cnt + 1):
            _price = i + price * j
            if _price > total:
                break
            if _price > M:
                M = _price
            dp[_price] += dp[i]
P = [1] * (total + 2)
P[0] = P[1] = 0
for i in range(2, int(total**0.5) + 1):
    if P[i]:
        for j in range(i * 2, total + 1, i):
            P[j] = 0
res = 0
for i in range(total + 1):
    if P[i]:
        res += dp[i]
print(res * zero)

n, k = map(int, input().split())

dp = [
    [[[0 for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)
]

ans = [0] * 31


def go(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False
    if dp[i][a][b][p]:
        return False
    dp[i][a][b][p] = True
    ans[i] = "A"
    if go(i + 1, a + 1, b, p):
        return True
    ans[i] = "B"
    if go(i + 1, a, b + 1, p + a):
        return True
    ans[i] = "C"
    if go(i + 1, a, b, p + a + b):
        return True
    return False


if go(0, 0, 0, 0):
    print("".join(ans[0:n]))
else:
    print(-1)

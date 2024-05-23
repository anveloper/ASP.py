import sys


def dfs(a, b, l, t):
    global n, p
    if l == n:
        if t == p:
            print("".join(s))
            sys.exit()
        else:
            return

    if memo.get((a, b, l, t)) is None:
        memo[(a, b, l, t)] = True
    else:
        return

    s[l] = "A"
    dfs(a + 1, b, l + 1, t)
    s[l] = "B"
    dfs(a, b + 1, l + 1, t + a)
    s[l] = "C"
    dfs(a, b, l + 1, t + a + b)


n, p = map(int, sys.stdin.readline().rstrip().split())
memo = {}
s = [""] * n

dfs(0, 0, 0, 0)
print(-1)

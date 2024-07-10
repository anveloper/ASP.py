import sys

input = sys.stdin.readline
A = sorted(tuple(map(int, input().split())) for _ in range(int(input())))
m = 20000
ans = 0
for _, y in A:
    if y < m:
        ans += 1
        m = y
print(ans)

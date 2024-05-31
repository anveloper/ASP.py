import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a = list(input().strip())
    d = {}
    tmp = 1
    for j in range(len(a)):
        if a[j] not in d:
            d[a[j]] = tmp
            a[j] = d[a[j]]
            tmp += 1
        else:
            a[j] = d[a[j]]
    lst.append("".join(map(str, a)))

ans = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if lst[i] == lst[j]:
            ans += 1

print(ans)

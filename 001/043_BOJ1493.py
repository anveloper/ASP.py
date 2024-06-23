import sys

input = sys.stdin.readline

l, w, h = map(int, input().split())
total_v = l * w * h
n = int(input())
cubes = []
for i in range(n):
    s, count = map(int, input().split())
    s = 2**s
    cubes.append([s * s * s, s, count])


cur_v = 0
ans = 0
cubes.sort(reverse=True)
for v, s, c in cubes:

    cur_v *= 8
    cur_c = (l // s) * (w // s) * (h // s) - cur_v
    cur_c = min(cur_c, c)
    ans += cur_c
    cur_v += cur_c

if cur_v == total_v:
    print(ans)
else:
    print(-1)

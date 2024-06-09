import sys

n, m = map(int, input().split(" "))
min_g = n + 1
max_s = 0
l = []
for i in range(n):
    guiter, able = sys.stdin.readline().rstrip().split(" ")
    able = able.replace("Y", "1")
    able = able.replace("N", "0")
    l.append(int(able, 2))


for i in range(1 << n):
    n_guitar = 0
    check = 0
    for j in range(n):
        if i & (1 << j):
            a = l[j]
            check = check | a
            n_guitar += 1
    if max_s < bin(check).count("1"):
        min_g = n_guitar
        max_s = bin(check).count("1")

    elif max_s == bin(check).count("1"):
        if min_g > n_guitar:
            min_g = n_guitar

if max_s == 0:
    print(-1)
else:
    print(min_g)

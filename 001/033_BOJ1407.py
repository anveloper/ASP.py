A, B = map(int, input().split())
A -= 1
a = A
for i in range(1, 50):
    a += (A // 2**i) * (2 ** (i - 1))

b = B
for i in range(1, 50):
    b += (B // 2**i) * (2 ** (i - 1))

print(b - a)

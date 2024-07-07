import math, sys

N, K = map(int, input().split())
len = len(str(N))
N, K = N // math.gcd(N, K), K // math.gcd(N, K)
tmp = N
for i in range(K):
    if tmp % K == 0:
        print(i + 1)
        sys.exit()
    tmp = (tmp * 10**len + N) % K
print(-1)

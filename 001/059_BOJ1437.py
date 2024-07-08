N = int(input())
M = 10007
if N < 5:
    print(N)
elif N % 3 == 0:
    print(pow(3, N // 3, M))
elif N % 3 == 1:
    print((pow(3, (N - 4) // 3, M) * 4) % M)
else:
    print((pow(3, (N - 2) // 3, M) * 2) % M)

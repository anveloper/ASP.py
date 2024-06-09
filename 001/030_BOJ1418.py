N = int(input())
K = int(input())

primeList = [True] * (N + 1)
for i in range(2, int(N**0.5) + 1):
    if primeList[i]:
        for j in range(2 * i, N + 1, i):
            primeList[j] = False
k_number = [1] * (N + 1)

for i in range(2, N + 1):
    if primeList[i] and i > K:
        for j in range(i, N + 1, i):
            k_number[j] = 0

print(sum(k_number) - 1)

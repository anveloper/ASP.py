from sys import stdin

MOD = 1_000_000


def mat_mul(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i, row in enumerate(m1):
        for j, col in enumerate(zip(*m2)):
            result[i][j] = sum([r * c for r, c in zip(row, col)]) % MOD
    return result


def get_power_of_mat(m, power):
    if power == 1:
        return m
    squared = get_power_of_mat(m, power // 2)
    if power % 2 == 0:
        return mat_mul(squared, squared)
    else:
        return mat_mul(m, mat_mul(squared, squared))


N = int(stdin.readline())
fibonacci_mat = [[1, 1], [1, 0]]
print(get_power_of_mat(fibonacci_mat, N + 1)[-1][-1])

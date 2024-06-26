import sys

input = sys.stdin.readline

DIRECTIONS = ((1, 0), (0, 1))
MOD = 1_000_007
N, M, C = map(int, input().split())

_map = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, C + 1):
    r, c = map(int, input().split())
    _map[r][c] = i

dp = [[[[0] * 51 for _ in range(51)] for _ in range(51)] for _ in range(51)]

if _map[1][1]:
    dp[1][_map[1][1]][1][1] = 1
else:
    dp[0][0][1][1] = 1


def find():
    for i in range(C + 1):
        for j in range(C + 1):
            for k in range(1, N + 1):
                for l in range(1, M + 1):
                    if not dp[i][j][k][l]:
                        continue
                    if l + 1 <= M and _map[k][l + 1] == 0:
                        dp[i][j][k][l + 1] = (dp[i][j][k][l + 1] + dp[i][j][k][l]) % MOD
                    elif l + 1 <= M and _map[k][l + 1] > j:
                        dp[i + 1][_map[k][l + 1]][k][l + 1] = (
                            dp[i + 1][_map[k][l + 1]][k][l + 1] + dp[i][j][k][l]
                        ) % MOD

                    if k + 1 <= N and _map[k + 1][l] == 0:
                        dp[i][j][k + 1][l] = (dp[i][j][k + 1][l] + dp[i][j][k][l]) % MOD
                    elif k + 1 <= N and _map[k + 1][l] > j:
                        dp[i + 1][_map[k + 1][l]][k + 1][l] = (
                            dp[i + 1][_map[k + 1][l]][k + 1][l] + dp[i][j][k][l]
                        ) % MOD


def main():
    find()
    ans = []
    for i in range(C + 1):
        temp = 0
        for j in range(C + 1):
            temp = (temp + dp[i][j][N][M]) % MOD
        ans.append(temp)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
